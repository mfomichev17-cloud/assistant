from voice.listen import listen
from voice.speak import speak
from brain.ai import ask_ai

from commands import (
    browser,
    calculator,
    steam,
    system,
    telegram,
    time_info,
    volume,
    weather,
)

COMMAND_MODULES = [
    browser,
    calculator,
    steam,
    system,
    telegram,
    time_info,
    volume,
    weather,
]


class Assistant:

    def __init__(self):
        self.active = True

    def listen_user(self):
        text = listen()
        return text.lower() if text else ""

    def handle_command(self, text):

        for module in COMMAND_MODULES:
            handled = module.handle(text, speak)

            if handled:
                return

        response = ask_ai(text)
        speak(response)

    def run(self):

        speak("Джарвис запущен")

        while self.active:

            text = self.listen_user()

            if text:
                if "выход" in text:
                    speak("До свидания")
                    break

                self.handle_command(text)