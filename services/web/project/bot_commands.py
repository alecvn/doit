greetings = ["hi ", "hello", "hello there", "hey", "howdy"]
inspire = ["inspire", "inspiration"]
report = ["report"]
info = ["info", "information", "how to", "what are the"]


def get_bot_response(context, external_url=""):
    command = context["text"]
    user = context["user"]
    responses = []

    if any(item in command.lower() for item in greetings):
        responses.append(f"Hello <@{user}>! :buff_spongebob:")
    elif any(item in command.lower() for item in inspire):
        responses.append(
            f"<@{user}> sounds like you need some encouragement! You know, my granbot always used to say \n{external_url}"
        )
        responses.append("\nThen again, he _was_ pretty senile...")
    elif any(item in command.lower() for item in report):
        responses.append(
            f"<@{user}> I'm sure you're doing well, but I haven't been paying that much attention yet..."
        )
    elif any(item in command.lower() for item in info):
        responses.append(
            f"<@{user}> what am I, some kind of scientist?! I'm telling you everything I know... for now..."
        )
    else:
        responses.append(f"<@{user}> what are you talking about?")
        responses.append(
            "> Do you want me to `inspire` you?\n> Do you want me to `report` on how you've been doing?\n> Do you want some `info` on today's tasks?"
        )
    return responses
