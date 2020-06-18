import os

import discord
from discord.ext import commands

from dotenv import load_dotenv


load_dotenv(verbose=True)
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")
CHANNEL_ID = int(os.getenv("DISCORD_CHANNEL_ID"))

bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    channel = bot.get_channel(CHANNEL_ID)
    print(f"{bot.user.name} has connected to Discord in channel #{channel}!")
    await send_msg("Hi I'm here", channel)


async def send_msg(msg, channel):
    await channel.send(msg)


# _loop = asyncio.get_event_loop()


# def on_TMessage(bot, update):
#     asyncio.run_coroutine_threadsafe(
#         broadcastMsg("discord", DChannel, update.message), _loop
#     )

# if __name__ == "__main__":
#     bot.run(TOKEN)
