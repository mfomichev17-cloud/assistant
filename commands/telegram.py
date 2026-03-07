import subprocess
import os

TELEGRAM_PATH = r"C:\Users\Mihail\AppData\Roaming\Telegram Desktop\Telegram.exe"

KEYWORDS_OPEN = [
    "открой телеграм",
    "открой telegram",
    "запусти телеграм"
]

KEYWORDS_CLOSE = [
    "закрой телеграм",
    "закрой telegram"
]


def open_telegram(speak):
    if os.path.exists(TELEGRAM_PATH):
        speak("Открываю Telegram")
        subprocess.Popen([TELEGRAM_PATH])
    else:
        speak("Я не нашёл Telegram на компьютере")


def close_telegram(speak):
    speak("Закрываю Telegram")
    os.system("taskkill /f /im Telegram.exe")


def handle(command, speak):
    for phrase in KEYWORDS_OPEN:
        if phrase in command:
            open_telegram(speak)
            return True

    for phrase in KEYWORDS_CLOSE:
        if phrase in command:
            close_telegram(speak)
            return True

    return False