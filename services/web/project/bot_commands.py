from sqlalchemy import func

from project.models import User, Reaction, Task, get_or_create

from project import db


greetings = ["hi ", "hello", "hello there", "hey", "howdy"]
inspire = ["inspire", "inspiration"]
report = ["report"]
info = ["info", "information", "how to", "what are the"]


def get_bot_response(context, external_url=""):
    command = context["text"]
    username = context["user"]
    user, created = get_or_create(
        db.session, User, slack_address=f"<@{username}>", slack_id=f"{username}"
    )
    responses = []

    if any(item in command.lower() for item in greetings):
        responses.append(f"Hello <@{username}>! :buff_spongebob:")
    elif any(item in command.lower() for item in inspire):
        responses.append(
            f"<@{username}> sounds like you need some encouragement! You know, my granbot always used to say \n{external_url}"
        )
        responses.append("\nThen again, he _was_ pretty senile...")
    elif any(item in command.lower() for item in report):
        first_reaction = Reaction.query.filter_by(user_id=user.id).first()
        if first_reaction:
            reactions = (
                Reaction.query.filter_by(user_id=user.id)
                .join(Task, Task.id == Reaction.task_id)
                .with_entities(func.count(Task.name), Task.name, Task.description)
                .group_by(Task.name, Task.description)
                .all()
            )
            base_str = f"<@{username}> here's a breakdown of your recorded activities since {first_reaction.created_at.strftime('%d %b %Y')} \n"
            reactions_str = ""
        for reaction in reactions:
            sets = reaction[0]
            activity = reaction[1]
            quantity, quantum = reaction[2].split(" ")
            reactions_str += f"> *{activity}* - _{sets}_ _sets_ of _{quantity}_ _{quantum}_ for a total of *{int(sets)*int(quantity)} {quantum}*\n"
            responses.append(base_str + reactions_str)
        else:
            responses.append(
                f"<@{username}> are you even trying?  Next time you complete a set, respond to the exercise with the emoji that best describes you..."
            )
    elif any(item in command.lower() for item in info):
        responses.append(
            f"<@{username}> what am I, some kind of scientist?! I'm telling you everything I know... for now..."
        )
    else:
        responses.append(f"<@{username}> what are you talking about?")
        responses.append(
            "> Do you want me to `inspire` you?\n> Do you want me to `report` on how you've been doing?\n> Do you want some `info` on today's tasks?"
        )
    return responses
