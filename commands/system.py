import os

PROCESSES = [
    "browser.exe",
    "steam.exe",
    "telegram.exe",
    "CalculatorApp.exe"
]


def close_all():
    for proc in PROCESSES:
        os.system(f"taskkill /f /im {proc}")


def handle(command: str, speak):
    if "закрой всё" in command or "закрой все" in command:
        speak("Закрываю все программы")
        close_all()
        return True

    return False