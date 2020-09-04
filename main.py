import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

user = "Bryan"

#Setting up text-to-speech voice and speaking rate
engine = pyttsx3.init()
voices = engine.getProperty("voices")
rate = engine.getProperty("rate")

engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 150)

#Converts text to speech and reads aloud the text put into the function
def speak(text):
    engine.say(text)
    engine.runAndWait()

#Greets user based on the time of the day
def greeting():
    hour = int(datetime.datetime.now().hour)

    if hour>0 and hour<12:
        speak("Good Morning" + user)
    elif hour>=12 and hour<18:
        speak("Good Afternoon" + user)
    else:
        speak("Good Evening" + user)

    speak("How may I help you today?")

speak("Initializing Jarvis...")
greeting()
