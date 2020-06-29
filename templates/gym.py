from rng import rng

from template import Exercise, Schedule

SCHEDULE = Schedule("0", "9-17", "*", "*", "*")
# SCHEDULE = Schedule("*", "*", "*", "*", "*")
EXERCISES = {
    "upper": [
        Exercise(
            "Push Ups",
            "20 reps",
            "https://media.giphy.com/media/Kjj5yTgDdiuvC/giphy.gif",
        ),
        Exercise(
            "Burpees",
            "10 reps",
            "https://media.giphy.com/media/23hPPMRgPxbNBlPQe3/giphy.gif",
        ),
        Exercise(
            "Shoulder Press Ups",
            "20 reps",
            "https://www.youtube.com/watch?v=KcvLM-Q4eFo",
        ),
        Exercise(
            "Inch Worms",
            "10 reps",
            "https://media.giphy.com/media/UTXzXAwUHGx8MDEtPS/giphy.gif",
        ),
        Exercise(
            "Decline Push-up", "10 reps", "https://www.youtube.com/watch?v=aq2xZxfrQlM"
        ),
        Exercise(
            "Tricep Dips",
            "20 reps",
            "https://media.giphy.com/media/13HOBYXe87LjvW/giphy.gif",
        ),
        Exercise(
            "Close-Grip Push Ups",
            "10 reps",
            "http://www.shapefit.com/pics/chest-exercises-push-ups-close-hand-position.gif",
        ),
        Exercise(
            "Kick Throughs",
            "20 reps",
            "https://raw.githubusercontent.com/alecvn/slack-gymbot/master/kick_through.gif",
        ),
    ],
    "legs": [
        Exercise(
            "Squats",
            "20 reps",
            "https://media.giphy.com/media/1qfKN8Dt0CRdCRxz9q/giphy.gif",
        ),
        Exercise(
            "Lunges",
            "20 reps",
            "https://media.giphy.com/media/l3q2Q3sUEkEyDvfPO/giphy.gif",
        ),
        Exercise(
            "High Knees",
            "30 seconds",
            "https://media.giphy.com/media/l0HlNOsSRC0Bts7iU/giphy.gif",
        ),
        Exercise(
            "Mountain Climbers",
            "30 seconds",
            "https://media.giphy.com/media/bWYc47O3jSef6/giphy.gif",
        ),
        Exercise(
            "Squat Jumps",
            "20 reps",
            "https://media.giphy.com/media/nmuUOAEvrKTLDT3yTn/giphy.gif",
        ),
        Exercise(
            "Side Lunges",
            "20 reps",
            "https://media.giphy.com/media/Pj0wnhvHp3AHMM5ILf/giphy.gif",
        ),
        Exercise(
            "Reverse Lunges",
            "20 reps",
            "https://media.giphy.com/media/3o6ozoyJ0IlfuEsuXu/giphy.gif",
        ),
    ],
    "core": [
        Exercise(
            "Sit Ups",
            "20 reps",
            "https://media.giphy.com/media/9EFCRjJF4EqB2/giphy.gif",
        ),
        Exercise(
            "Planks",
            "30 seconds",
            "https://media.giphy.com/media/xT8qBff8cRRFf7k2u4/giphy.gif",
        ),
        Exercise(
            "Side Planks",
            "30 seconds",
            "https://media.giphy.com/media/3o6gDUTsbepOYTqTRK/giphy.gif",
        ),
        Exercise(
            "Supermans",
            "20 reps",
            "https://media.giphy.com/media/PmPRDFY1ENYMo/giphy.gif",
        ),
        Exercise(
            "Leg Raises",
            "20 reps",
            "https://media.giphy.com/media/2LtUR24UvCZdC/giphy.gif",
        ),
        Exercise(
            "Bicycle Crunches",
            "20 reps",
            "https://media.giphy.com/media/TMNCtgJGJnV8k/giphy.gif",
        ),
    ],
}

# upper = rng.choice(EXERCISES["upper"])
# core = rng.choice(EXERCISES["core"])
# legs = rng.choice(EXERCISES["legs"])
# upper_msg = f"{upper.name} - {upper.description}"
# core_msg = f"{core.name} - {core.description}"
# legs_msg = f"{legs.name} - {legs.description}"

# MSG = upper_msg + core_msg + legs_msg
MSG = list(
    zip(EXERCISES.keys(), map(lambda x: rng.choice(EXERCISES[x]), EXERCISES.keys()))
)


# def get_message(exercise):
#     if exercise.rep_quantity == "reps":
#         return f"{exercise.num_reps} {exercise.name}"
#     else:
#         return f"{exercise.num_reps} {exercise.rep_quantity} of {exercise.name}"


# def get_image_json(title, group, attach_images):
#     chosen = random.choice(group)
#     text = get_message(chosen)

#     return {
#         "type": "image",
#         "image_url": chosen.image_url,
#         "alt_text": f"{title}: {text}",
#         "title": {"type": "plain_text", "text": f"{title}: {text}"},
#     }


# def get_text_json(title, group, attach_images):
#     chosen = random.choice(group)
#     text = get_message(chosen)

#     return {"type": "section", "text": {"type": "mrkdwn", "text": text}}
