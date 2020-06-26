import random
import pytz
import datetime


timezone = pytz.timezone("Africa/Johannesburg")
now = datetime.datetime.now(tz=timezone)

today = now.date()
random.seed(str(today))
rng = random
