from rng import rng

from template import Exercise, Schedule

SCHEDULE = Schedule("0", "12-16/4", "*", "*", "*")
# SCHEDULE = Schedule("*", "*", "*", "*", "*")

notes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
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
        f"{rng.choice(style)} 60bpm-90bpm/15bpm",
        "https://www.youtube.com/watch?v=NgY2S_zoPoc?t=2m26s",
    ),
    Exercise(
        f"Spider crawl",
        f"{rng.choice(style)} 60bpm-90bpm/15bpm",
        "https://www.youtube.com/watch?v=NgY2S_zoPoc?t=5m14s",
    ),
    Exercise(
        f"Chromatic scale",
        f"{rng.choice(style)} 60bpm-90bpm/15bpm",
        "https://www.youtube.com/watch?v=NgY2S_zoPoc?t=7m39s",
    ),
]
guitar_left_hand = [
    Exercise(
        f"Tremolo - Staccato",
        f"60bpm-90bpm/15bpm",
        "https://www.youtube.com/watch?v=K0ODw9QhILQ&t=3m59s",
    ),
    # Exercise(
    #     f"{rng.choice(notes)} {rng.choice(scales)} - along neck",
    #     f"{rng.choice(style)} down along neck, up along neck, skip to next string - 60bpm-90bpm/15bpm",
    #     "https://media.giphy.com/media/Kjj5yTgDdiuvC/giphy.gif",
    # ),
    # Exercise(
    #     f"{rng.choice(notes)} {rng.choice(scales)} - cross neck",
    #     f"{rng.choice(style)} down neck, up neck - 60bpm-90bpm/15bpm",
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
        "Strumming quarter notes",
        f"{rng.choice(notes)} {rng.choice(chord)} bare chord - 60bpm-90bpm/15bpm",
        "https://www.youtube.com/watch?v=WeJlUbFyes4&t=3m28s",
    ),
    # Exercise(
    #     "Strumming",
    #     f"{rng.choice(notes)} {rng.choice(chord)} bare chord - 60bpm-90bpm/15bpm",
    #     "https://www.youtube.com/watch?v=WeJlUbFyes4&t=3m28s",
    # ),
]
EXERCISES = {
    "warm_up": warm_up,
    "guitar_left_hand": guitar_left_hand,
    "guitar_right_hand": guitar_right_hand,
}

MSG = list(
    zip(EXERCISES.keys(), map(lambda x: rng.choice(EXERCISES[x]), EXERCISES.keys()))
)
