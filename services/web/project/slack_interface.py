import os
import logging
from threading import Thread

from flask import Response
from slack import WebClient
from slack.errors import SlackApiError
from slackeventsapi import SlackEventAdapter

from project import app, db
from project.bot_commands import greetings, inspire, report
from project.models import get_or_create, User

logging.getLogger().setLevel(logging.INFO)

SLACK_SIGNING_SECRET = os.getenv("SLACK_SIGNING_SECRET")
SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
slack_events_adapter = SlackEventAdapter(SLACK_SIGNING_SECRET, "/slack", app)
client = WebClient(token=SLACK_BOT_TOKEN)


# {
#     "token": "oh5twhzfE9D4nm4CjwzhGAbZ",
#     "team_id": "T0AMD6BK7",
#     "api_app_id": "A0166ELQ5NF",
#     "event": {
#         "type": "reaction_added",
#         "user": "U0AMD6BL5",
#         "item": {
#             "type": "message",
#             "channel": "G012N998QAZ",
#             "ts": "1594418905.000900",
#         },
#         "reaction": "rolling_on_the_floor_laughing",
#         "item_user": "U016CEC7XAR",
#         "event_ts": "1594419173.001200",
#     },
#     "type": "event_callback",
#     "event_id": "Ev016GKXG2MV",
#     "event_time": 1594419173,
#     "authed_users": ["U016CEC7XAR"],
# }
@slack_events_adapter.on("reaction_added")
def reaction_added(event_data):

    emoji = event_data["event"]["reaction"]

    print(emoji)


# {
#     "token": "oh5twhzfE9D4nm4CjwzhGAbZ",
#     "team_id": "T0AMD6BK7",
#     "api_app_id": "A0166ELQ5NF",
#     "event": {
#         "client_msg_id": "ba35ed36-52c5-4072-bf29-a5571f64eda3",
#         "type": "app_mention",
#         "text": "<@U016CEC7XAR> hello",
#         "user": "U0AMD6BL5",
#         "ts": "1594418903.000800",
#         "team": "T0AMD6BK7",
#         "blocks": [
#             {
#                 "type": "rich_text",
#                 "block_id": "YPT4W",
#                 "elements": [
#                     {
#                         "type": "rich_text_section",
#                         "elements": [
#                             {"type": "user", "user_id": "U016CEC7XAR"},
#                             {"type": "text", "text": " hello"},
#                         ],
#                     }
#                 ],
#             }
#         ],
#         "channel": "G012N998QAZ",
#         "event_ts": "1594418903.000800",
#     },
#     "type": "event_callback",
#     "event_id": "Ev016QL3CWCE",
#     "event_time": 1594418903,
#     "authed_users": ["U016CEC7XAR"],
# }
@slack_events_adapter.on("app_mention")
def handle_message(event_data):
    def send_reply(value):
        event_data = value
        message = event_data["event"]
        if message.get("subtype") is None:
            command = message.get("text")
            channel_id = message["channel"]

            if any(item in command.lower() for item in greetings):
                message = f"Hello <@{message['user']}>! :tada:"
                client.chat_postMessage(channel=channel_id, text=message)
            if any(item in command.lower() for item in inspire):
                message = "Sounds like you need some encouragement! You know, my grandmother always used to say \nhttps://generated.inspirobot.me/a/jDe2njWgez.jpg"
                client.chat_postMessage(channel=channel_id, text=message)
                message2 = "\nThen again, she _was_ pretty senile..."
                client.chat_postMessage(channel=channel_id, text=message2)
            if any(item in command.lower() for item in report):
                message = f"> <@{message['user']}>, you're\n> doing\n> amazingly!\n> newschool"
                client.chat_postMessage(channel=channel_id, text=message)

    user, created = get_or_create(
        db.session,
        User,
        slack_address=f"<@{event_data['event']['user']}>",
        slack_id=event_data["event"]["user"],
    )

    thread = Thread(target=send_reply, kwargs={"value": event_data})
    thread.start()

    db.session.commit()

    return Response(status=200)


async def send_msg(msg):
    try:
        client.chat_postMessage(channel="#test", text=msg)
    except SlackApiError as e:
        logging.warning(e)
