import datetime


def handle(command, speak):
    if "сколько сейчас времени" in command or "который час" in command:
        now = datetime.datetime.now()
        time_str = now.strftime("%H:%M")
        speak(f"Сейчас {time_str}")
        return True

    return False