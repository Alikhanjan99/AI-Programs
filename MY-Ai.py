import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
 
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning Sir !")
  
    elif hour>= 12 and hour<18:
        speak("Good Afternoon Sir !")  
  
    else:
        speak("Good Evening Sir !") 
  
    assname =("Jarvis 1 point o")
    speak("I am your Assistant")
    speak(assname)
     
 
def username():
    speak("What should i call you sir")
    uname = takeCommand()
    speak("Welcome Mister")
    speak(uname)
    columns = shutil.get_terminal_size().columns
     
    print("#####################".center(columns))
    print("Welcome Mr.", uname.center(columns))
    print("#####################".center(columns))
     
    speak("How can i Help you, Sir")
 
def takeCommand():
     
    r = sr.Recognizer()
     
    with sr.Microphone() as source:
         
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
  
    try:
        print("Recognizing...")   
        query = r.recognize_google(audio, language ='en-in')
        print(f"User said: {query}\n")
  
    except Exception as e:
        print(e)   
        print("Unable to Recognize your voice.") 
        return "None"
     
    return query
  
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
     
    # Enable low security in gmail
    server.login('your email id', 'your email password')
    server.sendmail('your email id', to, content)
    server.close()


        elif "Good Morning" in query:
            speak("A warm" +query)
            speak("How are you Mister")
            speak(assname)
 
        # most asked question from google Assistant
        elif "will you be my gf" in query or "will you be my bf" in query:  
            speak("I'm not sure about, may be you should give me some time")
 
        elif "how are you" in query:
            speak("I'm fine, glad you me that")
 
        elif "i love you" in query:
            speak("It's hard to understand")
 
        elif "what is" in query or "who is" in query:
             
            # Use the same API key
            # that we have generated earlier
            client = wolframalpha.Client("API_ID")
            res = client.query(query)
             
            try:
                print (next(res.results).text)
                speak (next(res.results).text)
            except StopIteration:
                print ("No results")
 
        # elif "" in query:
            # Command go here
            # For adding more commands
