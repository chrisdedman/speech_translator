from googletrans import Translator
import speech_recognition as sr
from sys import exit
import pyttsx3
import pyaudio
import os

r = sr.Recognizer()
micro = sr.Microphone(device_index=0)


# French Apple Speaker
def speakFR(command):
    engine = pyttsx3.init()
    voice_id = "com.apple.speech.synthesis.voice.thomas"
    engine.setProperty("voice", voice_id)
    # Sets speed percent, can be more than 100
    engine.setProperty("rate", 180)
    engine.setProperty("volume", 0.7)
    engine.say(command)
    engine.runAndWait()


# English Apple Speaker
def speakEN(command):
    engine = pyttsx3.init()
    voice_id = "com.apple.speech.synthesis.voice.samantha"
    engine.setProperty("voice", voice_id)
    # Sets speed percent, can be more than 100
    engine.setProperty("rate", 180)
    engine.setProperty("volume", 0.7)
    engine.say(command)
    engine.runAndWait()


# Command in English
def CommandEN():

    with micro as source:

        print("I'm listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("I'm recognizing...")
        #  Add you code language here
        MyTextEN = r.recognize_google(audio, language="en-US")
        p = Translator()
        # Add the language you want to translate here
        My = p.translate(MyTextEN, dest="french")
        translated = str(My.text)
        print("Il a dit: ", translated)
        speakFR("Il a dit: " + translated)
        print(f"You said: {MyTextEN}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognizing your voice.")
        return "None"

    return MyTextEN


# Command in French
def CommandFR():

    with micro as source:

        print("J'ecoute...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Je traduit...")
        #  Add you code language here
        MyTextEN = r.recognize_google(audio, language="fr-FR")  
        p = Translator()
        # Add the language you want to translate here
        My = p.translate(MyTextFR, dest="english")
        translated = str(My.text)
        print("He said: ", translated)
        speakEN("He said: " + translated)
        print(f"Tu a dit: {MyTextFR}\n")

    except Exception as e:
        print(e)
        print("Incapable de reconnaitre votre voix.")
        return "None"

    return MyTextFR


# Welcome in the program message
def welcome():
    hello = "Welcome to the speech translator! Start to speak in English."
    print(hello)
    speakEN(hello)


# Run the program
if __name__ == "__main__":
    os.system("clear")
    welcome()
    while 1:
        MyTextEN = CommandEN().lower()
        if "stop translate" in MyTextEN:
            exit(0)
        speakFR("Parler en Francais")
        MyTextFR = CommandFR().lower()
        if "arrête de traduire" in MyTextFR:
            exit(0)
        speakEN("Speak in English")
