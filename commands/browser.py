import subprocess
import webbrowser
import time
import os

YANDEX_PATH = r"C:\Users\%USERNAME%\AppData\Local\Yandex\YandexBrowser\Application\browser.exe"


def open_browser():
    subprocess.Popen(YANDEX_PATH, shell=True)


def close_browser():
    os.system("taskkill /f /im browser.exe")


def open_vk_video():
    open_browser()
    time.sleep(3)
    webbrowser.open("https://vk.com/video")


def handle(command: str, speak):
    if "вк видео" in command:
        speak("Открываю VK Видео")
        open_vk_video()
        return True

    if "закрой вк видео" in command:
        speak("Закрываю VK Видео")
        close_browser()
        return True

    if "открой браузер" in command or "открой яндекс" in command:
        speak("Открываю браузер")
        open_browser()
        return True

    if "закрой браузер" in command:
        speak("Закрываю браузер")
        close_browser()
        return True

    return False