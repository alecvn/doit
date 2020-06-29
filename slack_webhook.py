import requests
import datetime
import os
import pytz
import json
from dotenv import load_dotenv

load_dotenv(verbose=True)
WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")
CHANNEL_NAME = os.getenv("SLACK_CHANNEL_NAME")
USERNAME = os.getenv("SLACK_USERNAME")


def get_thumbnail(media_url):
    if media_url[-4:] == ".gif":
        return media_url
    elif "youtube" in media_url:
        youtube_id = media_url.split("watch?v=")[1]
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
    accessory = {}
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
        block.append(get_actions_block())

    return blocks


def get_inspirational_url():
    return str(requests.get("https://inspirobot.me/api?generate=true").content, "utf-8")


def send_msg(msgs):
    if not WEBHOOK_URL:
        raise ValueError("Add the SLACK_WEBHOOK_URL environment var plox")
    timezone = pytz.timezone("Africa/Johannesburg")
    now = datetime.datetime.now(tz=timezone)

    start_hour = 9
    end_hour = 17
    current_hour = now.hour
    attach_images = current_hour == start_hour
    inspirational_hours = [10, 13, 16]
    inspirational_image_url = (
        get_inspirational_url() if current_hour in inspirational_hours else ""
    )

    blocks = get_blocks(
        msgs,
        inspirational_image_url=inspirational_image_url,
        show_media=current_hour == start_hour,
    )

    # header = f"*<{inspirational_image_url}|Some text>*"

    msg_json = {
        "channel": CHANNEL_NAME,
        "username": USERNAME,
        "icon_emoji": "aw_yeah",
        "blocks": blocks,
    }
    print(msg_json)

    return requests.post(WEBHOOK_URL, json=msg_json)
