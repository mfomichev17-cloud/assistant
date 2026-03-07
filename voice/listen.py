import speech_recognition as sr

def listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("🎤 Слушаю...")
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language="ru-RU")
        print("🧑 Ты:", text)
        return text
    except:
        return ""