# from rng import rng as random

# from template import Exercise, Schedule

import collections
import random
import pytz
import datetime


timezone = pytz.timezone("Africa/Johannesburg")
now = datetime.datetime.now(tz=timezone)

today = now.date()
random.seed(str(today))


Schedule = collections.namedtuple(
    "Schedule", ["min", "hour", "day", "month", "day_of_week"]
)
Exercise = collections.namedtuple("Exercise", ["name", "description", "media_url"])


SCHEDULE = Schedule("0", "12-16/4", "*", "*", "*")
# SCHEDULE = Schedule("*", "*", "*", "*", "*")

notes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
note_duration = ["quarter", "third"]
scales = [
    "Major (Ionian)",
    # "Dorian",
    # "Phrygian",
    # "Lydian",
    # "Mixolydian",
    "Minor (Aeolian)",
    # "Locrian",
    # "Harmonic Minor",
    # "Melodic Minor",
]
chord = ["Major", "Minor"]
style = ["Pick", "Fingers"]
warm_up = [
    Exercise(
        f"String crossings",
        f"{random.choice(style)} 60bpm-90bpm/15bpm",
        "https://www.youtube.com/watch?v=NgY2S_zoPoc&t=2m26s",
    ),
    Exercise(
        f"Spider crawl",
        f"{random.choice(style)} 60bpm-90bpm/15bpm",
        "https://www.youtube.com/watch?v=NgY2S_zoPoc&t=5m14s",
    ),
    Exercise(
        f"Chromatic scale",
        f"{random.choice(style)} 60bpm-90bpm/15bpm",
        "https://www.youtube.com/watch?v=NgY2S_zoPoc&t=7m39s",
    ),
]
guitar_left_hand = [
    # Exercise(
    #     f"{random.choice(notes)} {random.choice(scales)} - along neck",
    #     f"{random.choice(style)} down along neck, up along neck, skip to next string - 60bpm-90bpm/15bpm",
    #     "https://media.giphy.com/media/Kjj5yTgDdiuvC/giphy.gif",
    # ),
    # Exercise(
    #     f"{random.choice(notes)} {random.choice(scales)} - cross neck",
    #     f"{random.choice(style)} down neck, up neck - 60bpm-90bpm/15bpm",
    #     "https://media.giphy.com/media/23hPPMRgPxbNBlPQe3/giphy.gif",
    # ),
]
guitar_right_hand = [
    # Exercise(
    #     "Arpeggio's",
    #     "60bpm-90bpm/15bpm",
    #     "https://media.giphy.com/media/Kjj5yTgDdiuvC/giphy.gif",
    # ),
    Exercise(
        f"Strumming {random.choice(note_duration)} notes",
        f"{random.choice(notes)} {random.choice(chord)} barre chord - 60bpm-90bpm/15bpm",
        "https://www.youtube.com/watch?v=WeJlUbFyes4&t=3m28s",
    ),
    Exercise(
        f"Tremolo - Staccato",
        f"60bpm-90bpm/15bpm",
        "https://www.youtube.com/watch?v=K0ODw9QhILQ&t=3m59s",
    ),
]
EXERCISES = {
    "warm_up": warm_up,
    "guitar_left_hand": guitar_left_hand,
    "guitar_right_hand": guitar_right_hand,
}

MSG = list(
    zip(EXERCISES.keys(), map(lambda x: random.choice(EXERCISES[x]), EXERCISES.keys()))
)
print(MSG)
