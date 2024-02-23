import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

engine.setProperty("rate", 150)   
engine.setProperty("volume", 0.8) 

with sr.Microphone() as source:
    print("Listening...")
    audio = recognizer.listen(source)

try:
    text = recognizer.recognize_google(audio)  # Get transcribed text
    print("You said:", text)

    # Speak the transcribed text
    engine.say(text)
    engine.runAndWait()

except sr.UnknownValueError:
    print("Sorry, I could not understand.")


    