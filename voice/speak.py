import pyttsx3

engine = pyttsx3.init("sapi5")

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

engine.setProperty("rate", 195)
engine.setProperty("volume", 0.9)

def speak(text):
    print("🤖 Джарвис:", text)

    engine.say(text)
    engine.runAndWait()