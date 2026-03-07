import subprocess


def open_calculator():
    subprocess.Popen("calc", shell=True)


def close_calculator():
    subprocess.Popen("taskkill /f /im CalculatorApp.exe", shell=True)


def handle(command: str, speak):
    if "открой калькулятор" in command or "запусти калькулятор" in command:
        speak("Открываю калькулятор")
        open_calculator()
        return True

    if "закрой калькулятор" in command:
        speak("Закрываю калькулятор")
        close_calculator()
        return True

    return False