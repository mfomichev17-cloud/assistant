import ctypes

VK_VOLUME_MUTE = 0xAD
VK_VOLUME_DOWN = 0xAE
VK_VOLUME_UP = 0xAF


def press_key(key):
    ctypes.windll.user32.keybd_event(key, 0, 0, 0)
    ctypes.windll.user32.keybd_event(key, 0, 2, 0)


def volume_up():
    press_key(VK_VOLUME_UP)


def volume_down():
    press_key(VK_VOLUME_DOWN)


def volume_mute():
    press_key(VK_VOLUME_MUTE)


def handle(command, speak):
    command = command.lower()

    if "прибавь звук" in command or "сделай погромче" in command:
        speak("Делаю громче")
        volume_up()
        return True

    if "убавь звук" in command or "сделай потише" in command:
        speak("Делаю тише")
        volume_down()
        return True

    if "выключи звук" in command or "без звука" in command:
        speak("Выключаю звук")
        volume_mute()
        return True

    if "включи звук" in command:
        speak("Включаю звук")
        volume_mute()
        return True

    return False