import os

import discord
from discord.ext import commands

from dotenv import load_dotenv

from lib import get_thumbnail


load_dotenv(verbose=True)
TOKEN = os.getenv("DISCORD_TOKEN")
# GUILD = os.getenv("DISCORD_GUILD")
CHANNEL_ID = int(os.getenv("DISCORD_CHANNEL_ID"))

bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print(f"{bot.user.name} has connected")
    await send_msgs("Hi I'm here", bot)


async def send_msgs(msg, _bot):
    for category_channel in bot.get_all_channels():
        await send_msg(msg, _bot, category_channel.id)


async def send_msg(msg, _bot, channel_id):

    if isinstance(msg, str):
        channel = _bot.get_channel(channel_id)
        try:
            await channel.send(msg)
        except AttributeError:
            pass
    else:
        embed = discord.Embed(title="Guitar", description="")
        # embed.set_image(url=get_thumbnail(item.media_url))
        # embed.set_thumbnail(url=get_thumbnail(item.media_url))
        # embed.set_video(url=item.media_url)

        # embed.set_author(name=group)
        for obj in msg:
            group, item = obj
            # print(get_thumbnail(item.media_url))

            embed.add_field(
                name=group.capitalize().replace("_", " "),
                value=item.name + "\n" + item.description + "\n" + item.media_url,
                inline=False,
            )

        channel = _bot.get_channel(channel_id)
        try:
            await channel.send(embed=embed)
        except AttributeError:
            pass
