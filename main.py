import asyncio
import aiocron
from aiocron import crontab

from discord_bot import bot as d_bot, send_msgs as discord_send_msgs, CHANNEL_ID, TOKEN
from slack_webhook import send_msg as slack_send_msg

from templates.guitar import (
    EXERCISES as GUITAR_EXERCISES,
    SCHEDULE as GUITAR_SCHEDULE,
    MSG as GUITAR_MSG,
)

from templates.gym import (
    EXERCISES as GYM_EXERCISES,
    SCHEDULE as GYM_SCHEDULE,
    MSG as GYM_MSG,
)


async def send_discord_message(msg):
    await discord_send_msgs(msg, d_bot)


async def send_slack_message(msg):
    slack_send_msg(msg)


crontab(
    " ".join(GUITAR_SCHEDULE), func=lambda: send_discord_message(GUITAR_MSG), start=True
)
crontab(" ".join(GYM_SCHEDULE), func=lambda: slack_send_msg(GYM_MSG), start=True)


async def wake_time():
    await asyncio.sleep(10)


def main():
    loop = asyncio.get_event_loop()

    loop.create_task(d_bot.start(TOKEN))
    print("Bot joined")
    loop.run_until_complete(wake_time())
    print("Bot awake")
    loop.run_forever()


if __name__ == "__main__":
    main()
