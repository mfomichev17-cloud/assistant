import subprocess
import os

STEAM_EXE = r"C:\Program Files (x86)\Steam\steam.exe"

STEAM_OPEN = ["открой стим", "запусти стим", "открой Steam", "открой steam"]
STEAM_CLOSE = ["закрой стим", "закрой Steam", "закрой steam"]
BIG_PICTURE_ON = ["открой игровой режим", "включи игровой режим", "игровой режим"]
BIG_PICTURE_OFF = ["закрой игровой режим", "обычный режим"]


def open_steam():
    subprocess.Popen(STEAM_EXE)


def close_steam():
    os.system("taskkill /f /im steam.exe")
    os.system("taskkill /f /im steamwebhelper.exe")


def open_big_picture():
    subprocess.Popen([STEAM_EXE, "-bigpicture"])


def close_big_picture():
    subprocess.Popen([STEAM_EXE, "-silent"])


def handle(command: str, speak):
    for phrase in STEAM_OPEN:
        if phrase in command:
            speak("Открываю Steam")
            open_steam()
            return True

    for phrase in BIG_PICTURE_ON:
        if phrase in command:
            speak("Включаю игровой режим")
            open_big_picture()
            return True

    for phrase in BIG_PICTURE_OFF:
        if phrase in command:
            speak("Выключаю игровой режим")
            close_big_picture()
            return True

    for phrase in STEAM_CLOSE:
        if phrase in command:
            speak("Закрываю Steam")
            close_steam()
            return True

    return False