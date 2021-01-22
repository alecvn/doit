import asyncio
import logging
import os

from aiocron import crontab
from project.http import process_batch
from project.models import User
from project.slack_interface import send_msg as slack_send_msg
from project.slack_interface import send_weekly_update
from project.templates.gym import EXERCISES as GYM_EXERCISES
from project.templates.gym import SCHEDULE as GYM_SCHEDULE
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
Session = sessionmaker(bind=engine)
session = Session()

logging.getLogger().setLevel(logging.INFO)


# crontab(" ".join(GYM_SCHEDULE), func=lambda: slack_send_msg(GYM_MSG), start=True)
crontab(
    " ".join(GYM_SCHEDULE),
    func=lambda: process_batch(
        [lambda: slack_send_msg(session, GYM_EXERCISES, send_as_blocks=True)]
    ),
    start=True,
)

crontab(
    "30 15 * * 5",
    func=lambda: process_batch(
        [lambda: send_weekly_update(session, send_as_blocks=True)]
    ),
    start=True,
)

loop = asyncio.get_event_loop()
loop.run_forever()
