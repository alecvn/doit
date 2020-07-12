import asyncio
from aiocron import crontab

from project.http import process_batch
from project.slack_interface import send_msg as slack_send_msg

from project.templates.gym import (
    EXERCISES as GYM_EXERCISES,
    SCHEDULE as GYM_SCHEDULE,
    MSG as GYM_MSG,
)

# crontab(" ".join(GYM_SCHEDULE), func=lambda: slack_send_msg(GYM_MSG), start=True)
crontab(
    " ".join(GYM_SCHEDULE),
    func=lambda: process_batch([lambda: slack_send_msg(GYM_MSG, send_as_blocks=True)]),
    start=True,
)

loop = asyncio.get_event_loop()
loop.run_forever()
