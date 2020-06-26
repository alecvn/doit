import collections

Schedule = collections.namedtuple(
    "Schedule", ["min", "hour", "day", "month", "day_of_week"]
)
Exercise = collections.namedtuple("Exercise", ["name", "description", "media_url"])

# EXERCISES = [{"group_name": [Exercise("name", "description", "media_url")]}]
# SCHEDULE = Schedule("min", "hour", "day", "month" "day_of_week")
