import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

print("Initializing J.A.R.V.I.S")

#Setting up text-to-speech voice and speaking rate
engine = pyttsx3.init()
voices = engine.getProperty("voices")
rate = engine.getProperty("rate")

engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 120)

#Converts text to speech and reads aloud the text put into the function
def speak(text):
    engine.say(text)
    engine.runAndWait()

speak("Hello")
