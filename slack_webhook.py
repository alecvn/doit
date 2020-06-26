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


def send_msg(msg):
    if not WEBHOOK_URL:
        raise ValueError("Add the SLACK_WEBHOOK_URL environment var plox")
    timezone = pytz.timezone("Africa/Johannesburg")
    now = datetime.datetime.now(tz=timezone)

    start_hour = 9
    end_hour = 17
    current_hour = now.hour
    attach_images = current_hour == start_hour

    pretexts = {
        start_hour: "*Good morning sunshine! *\n Now",
        10: "*Just before you have that cookie...*",
        12: "*Lunch is going to taste so much better if you *",
        13: "*Belly full or barely full, it doesn't change the fact you need to *",
        16: "*You're almost there big boy... *\n Now",
        end_hour: "*If you've made it this far, you might as well go all the way...*",
    }

    start_pretext = pretexts.get(current_hour, "Just")
    pretext = f"{start_pretext} drop and give me: \n "

    # if current_hour == start_hour:
    #     get_block = get_image_json
    # else:
    #     get_block = get_text_json

    json_request = {
        "channel": CHANNEL_NAME,
        "username": USERNAME,
        "blocks": [
            {"type": "section", "text": {"type": "mrkdwn", "text": pretext}},
            {"type": "section", "text": {"type": "mrkdwn", "text": msg}}
            # get_block("Upper Body", EXERCISES["upper"], attach_images),
            # get_block("Core", EXERCISES["core"], attach_images),
            # get_block("Legs", EXERCISES["legs"], attach_images),
        ],
    }

    return requests.post(WEBHOOK_URL, json=json_request)
