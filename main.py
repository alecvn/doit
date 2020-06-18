import asyncio

from discord_bot import bot, send_msg, CHANNEL_ID, TOKEN


async def wake_time():
    await asyncio.sleep(10)


def main():
    loop = asyncio.get_event_loop()
    loop.create_task(bot.start(TOKEN))
    print("bot joined")
    loop.run_until_complete(wake_time())
    print("bot awake")
    loop.create_task(send_msg("Do it, do it now!!!", bot.get_channel(CHANNEL_ID)))
    loop.run_forever()


if __name__ == "__main__":
    main()
