import os
import pytz
import datetime
import logging
from threading import Thread
import requests

from flask import Response
from slack import WebClient
from slack.errors import SlackApiError
from slackeventsapi import SlackEventAdapter

from project import app, db
from project.bot_commands import get_bot_response
from project.models import get_or_create, User, Task


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
    user, created = get_or_create(
        db.session,
        User,
        slack_address=f"<@{event_data['event']['user']}>",
        slack_id=event_data["event"]["user"],
    )
    task = Task(name="test", user_id=user.id, completed=True)
    db.session.add(task)
    db.session.commit()
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
            # command = message.get("text")
            channel_id = message["channel"]
            bot_responses = get_bot_response(
                message, external_url=get_inspirational_url()
            )
            for response in bot_responses:
                client.chat_postMessage(channel=channel_id, text=response)

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


def get_thumbnail(media_url):
    if media_url[-4:] == ".gif":
        return media_url
    elif "youtube" in media_url:
        youtube_id = media_url.split("watch?v=")[1]
        youtube_id = youtube_id.split("?t=")[0]
        return f"https://img.youtube.com/vi/{youtube_id}/1.jpg"
    else:
        raise "UnsupportedUrl: Url is not a Gif nor a Youtube video"


def get_text(group, name, description, image_url=""):
    return f"*{group.capitalize()}*\n<{image_url}|{name}> - {description}"


def get_actions_block():
    return {
        "type": "actions",
        "elements": [
            {
                "type": "button",
                "text": {"type": "plain_text", "emoji": True, "text": "Done!"},
                "style": "primary",
                "value": "completed",
            }
        ],
    }


def get_image_block(image_url, alt_text):
    return {
        "type": "image",
        "image_url": image_url,
        "alt_text": f"{alt_text} thumbnail",
    }


def get_main_block(group, name, description, media_url, show_media=False):
    if show_media:
        return {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": get_text(group, name, description, media_url),
            },
            "accessory": {
                "type": "image",
                "image_url": get_thumbnail(media_url),
                "alt_text": f"{name} thumbnail",
            },
        }
    else:
        return {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": get_text(group, name, description, media_url),
            },
        }


def get_blocks(objs, inspirational_image_url="", show_media=False, show_actions=False):
    blocks = []

    if inspirational_image_url != "":
        blocks.append(get_image_block(inspirational_image_url, "inspiration"))

    for obj in objs:
        group, item = obj
        blocks.append(
            get_main_block(
                group, item.name, item.description, item.media_url, show_media
            )
        )

    if show_actions:
        blocks.append(get_actions_block())

    return blocks


def get_inspirational_url():
    return str(requests.get("https://inspirobot.me/api?generate=true").content, "utf-8")


def get_msg(msgs):
    timezone = pytz.timezone("Africa/Johannesburg")
    now = datetime.datetime.now(tz=timezone)

    # start_hour = 9
    # end_hour = 17
    current_hour = now.hour
    # attach_images = current_hour == start_hour
    inspirational_hours = []
    inspirational_image_url = (
        get_inspirational_url() if current_hour in inspirational_hours else ""
    )

    blocks = get_blocks(
        msgs, inspirational_image_url=inspirational_image_url, show_media=True
    )

    # header = f"*<{inspirational_image_url}|Some text>*"

    # msg_json = {
    #     "channel": CHANNEL_NAME,
    #     "username": USERNAME,
    #     "icon_emoji": "aw_yeah",
    #     "blocks": blocks,
    # }
    # print(msg_json)

    # return requests.post(WEBHOOK_URL, json=msg_json)
    return blocks


async def send_msg(msg, send_as_blocks=False):
    try:
        if send_as_blocks:
            blocks_from_message = get_msg(msg)
            client.chat_postMessage(channel="#test", blocks=blocks_from_message)
            client.chat_postMessage(channel="#workout", blocks=blocks_from_message)
        else:
            client.chat_postMessage(channel="#test", text=msg)
            client.chat_postMessage(channel="#workout", text=msg)
    except SlackApiError as e:
        logging.warning(e)
