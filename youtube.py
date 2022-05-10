import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
from PyDictionary import PyDictionary

import numpy as np

from youtube_search import YoutubeSearch
import pafy
import vlc
import time
import json

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

print("Speak: ")
search=takeCommand().lower
results = json.loads(YoutubeSearch(search, max_results=10).to_json())

# print(results['videos'][0]['link'])
title,link,id=results['videos'][0]['title'],"https://www.youtube.com/"+results['videos'][0]['link'],results['videos'][0]['id']

url = link
video = pafy.new(url)
best = video.getbest()
playurl = best.url
Instance = vlc.Instance()
player = Instance.media_player_new()
Media = Instance.media_new(playurl)
Media.get_mrl()
player.set_media(Media)
player.play()
c=int(input("ENter: "))
if c==1:
    time.sleep(1)
