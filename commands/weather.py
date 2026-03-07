import requests
from datetime import datetime

API_KEY = "7389ae3bf0e100b4ab5f04ea6e4edc6f"
CITY = "Nizhny Novgorod"

KEYWORDS_NOW = [
    "какая погода",
    "какая сейчас погода",
    "погода",
    "сколько градусов"
]

KEYWORDS_TOMORROW = [
    "погода завтра",
    "какая погода завтра",
    "что будет завтра"
]


def get_weather_now():
    url = (
        "https://api.openweathermap.org/data/2.5/weather"
        f"?q={CITY}&appid={API_KEY}&units=metric&lang=ru"
    )

    r = requests.get(url, timeout=5)
    if r.status_code != 200:
        return None

    data = r.json()

    temp = round(data["main"]["temp"])
    feels = round(data["main"]["feels_like"])
    desc = data["weather"][0]["description"]

    return temp, feels, desc


def get_weather_tomorrow():
    url = (
        "https://api.openweathermap.org/data/2.5/forecast"
        f"?q={CITY}&appid={API_KEY}&units=metric&lang=ru"
    )

    r = requests.get(url, timeout=5)
    if r.status_code != 200:
        return None

    data = r.json()

    tomorrow = datetime.now().date().day + 1

    for item in data["list"]:
        dt = datetime.fromtimestamp(item["dt"])
        if dt.hour == 12 and dt.day == tomorrow:
            temp = round(item["main"]["temp"])
            desc = item["weather"][0]["description"]
            return temp, desc

    return None


def handle(command, speak):
    # --- ПОГОДА СЕЙЧАС ---
    for phrase in KEYWORDS_NOW:
        if phrase in command:
            weather = get_weather_now()
            if not weather:
                speak("Не удалось получить погоду.")
                return True

            temp, feels, desc = weather
            speak(
                f"В Нижнем Новгороде сейчас {desc}. "
                f"Температура {temp} градусов, "
                f"ощущается как {feels}."
            )
            return True

    # --- ПОГОДА ЗАВТРА ---
    for phrase in KEYWORDS_TOMORROW:
        if phrase in command:
            weather = get_weather_tomorrow()
            if not weather:
                speak("Не удалось получить прогноз на завтра.")
                return True

            temp, desc = weather
            speak(
                f"Завтра в Нижнем Новгороде ожидается {desc}, "
                f"температура около {temp} градусов."
            )
            return True

    return False