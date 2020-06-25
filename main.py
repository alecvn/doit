import asyncio
import aiocron
from aiocron import crontab

from discord_bot import bot, send_msg, CHANNEL_ID, TOKEN

# from slack_webhook import *


# @aiocron.crontab("* * * * *")
async def sendMessage(msg):
    await send_msg(msg, bot.get_channel(CHANNEL_ID))


# for file in templates:
# import EXERCISES, SCHEDULE
crontab("* * * * *", func=lambda: sendMessage("Do eet"), start=True)
crontab("* * * * *", func=lambda: sendMessage("Do two"), start=True)


async def wake_time():
    await asyncio.sleep(10)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(bot.start(TOKEN))
    print("bot joined")
    loop.run_until_complete(wake_time())
    print("bot awake")

    loop.run_forever()
