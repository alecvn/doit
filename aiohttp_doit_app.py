import os

from aiohttp import web

from slackeventsapi import SlackEventAdapter

from threading import Thread

from slack import WebClient

SLACK_SIGNING_SECRET = os.getenv("SLACK_SIGNING_SECRET")
SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")

client = WebClient(token=SLACK_BOT_TOKEN)

greetings = ["hi", "hello", "hello there", "hey"]


async def index(request):
    return web.Response(text="Welcome home!")


async def post(request):
    params = await request.json()
    print("#############Params##################")
    print(params)
    return web.Response(text=params["challenge"])

doit = web.Application()
doit.router.add_get("/", index)
doit.router.add_post("/slack", post)


slack_events_adapter = SlackEventAdapter(
    SLACK_SIGNING_SECRET, "/slack/events", doit
)


@slack_events_adapter.on("app_mention")
def handle_message(event_data):
    def send_reply(value):
        event_data = value
        message = event_data["event"]
        if message.get("subtype") is None:
            command = message.get("text")
            channel_id = message["channel"]
            if any(item in command.lower() for item in greetings):
                message = (
                    "Hello <@%s>! :tada:"
                    % message["user"]  # noqa
                )
                client.chat_postMessage(channel=channel_id, text=message)
    thread = Thread(target=send_reply, kwargs={"value": event_data})
    thread.start()
    return doit.Response(status=200)
