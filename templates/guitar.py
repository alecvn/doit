from rng import rng

from template import Exercise, Schedule

# SCHEDULE = Schedule("0", "10-18/2", "*", "*", "*")
SCHEDULE = Schedule("*", "*", "*", "*", "*")

notes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
scales = [
    "Ionian",
    "Dorian",
    "Phrygian",
    "Lydian",
    "Mixolydian",
    "Aeolian",
    "Locrian",
    "Harmonic Minor",
    "Melodic Minor",
]
style = ["Pick", "Fingers"]
guitar_left_hand = [
    Exercise(
        f"{rng.choice(notes)} {rng.choice(scales)} - along neck",
        f"{rng.choice(style)} down along neck, up along neck, skip to next string - 60bpm-90bpm/15bpm",
        "https://media.giphy.com/media/Kjj5yTgDdiuvC/giphy.gif",
    ),
    Exercise(
        f"{rng.choice(notes)} {rng.choice(scales)} - cross neck",
        f"{rng.choice(style)} down neck, up neck - 60bpm-90bpm/15bpm",
        "https://media.giphy.com/media/23hPPMRgPxbNBlPQe3/giphy.gif",
    ),
]
guitar_right_hand = [
    Exercise(
        "Arpeggio's",
        "60bpm-90bpm/15bpm",
        "https://media.giphy.com/media/Kjj5yTgDdiuvC/giphy.gif",
    ),
    Exercise(
        "Spider crawls - along neck",
        rng.choice(style) + " " + "- 60bpm-90bpm/15bpm",
        "https://media.giphy.com/media/Kjj5yTgDdiuvC/giphy.gif",
    ),
]
EXERCISES = {
    "guitar_left_hand": guitar_left_hand,
    "guitar_right_hand": guitar_right_hand,
}


lh = rng.choice(EXERCISES["guitar_left_hand"])
rh = rng.choice(EXERCISES["guitar_right_hand"])
lh_msg = f"{lh.name} - {lh.description}"
rh_msg = f"{rh.name} - {rh.description}"
MSG = lh_msg + rh_msg
