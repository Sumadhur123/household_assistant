import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
from PyDictionary import PyDictionary

import numpy as np

# You Tube
from youtube_search import YoutubeSearch
import pafy
import vlc
import time
import json

Instance = vlc.Instance()
player = Instance.media_player_new()
dictionary=PyDictionary()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you")       

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

def Youtube():
    try:
        print("Speak For The Search: ")
        search=takeCommand().lower()
        results = json.loads(YoutubeSearch(search, max_results=10).to_json())

        # print(results['videos'][0]['link'])
        title,link,id=results['videos'][0]['title'],"https://www.youtube.com/"+results['videos'][0]['link'],results['videos'][0]['id']

        url = link
        video = pafy.new(url)
        best = video.getbest()
        playurl = best.url
        
        
        Media = Instance.media_new(playurl)
        Media.get_mrl()
        player.set_media(Media)
        player.play()
        time.sleep(10)
    except IndexError:
        print("Network Connection Issue!!")
        return 
def google_search():

    term=takeCommand()
    tabUrl = "https://www.google.com/search?q="+ term


    webbrowser.open(tabUrl)
    
def open_dictionary():
    dictionary=PyDictionary()
    print("speak the word")
    word=takeCommand()

    
    print("The meaning of"+ word + " is")
    speak("The meaning of"+ word + " is")
    print(dictionary.meaning(word))
        
    speak(dictionary.meaning(word))

   
    

def weather():
    # Python program to find current 
# weather details of any city 
# using openweathermap api 

# import required modules 
    import requests, json 

    # Enter your API key here 
    api_key = "942a820f84b913bd41af2937dc27a3a7"

    # base_url variable to store url 
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    # Give city name 
    print("which city's weather you want to know")
    speak("which city's weather you want to know")
    city_name = takeCommand()

    # complete_url variable to store 
    # complete url address 
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name 

    # get method of requests module 
    # return response object 
    response = requests.get(complete_url) 

    # json method of response object 
    # convert json format data into 
    # python format data 
    x = response.json() 

    # Now x contains list of nested dictionaries 
    # Check the value of "cod" key is equal to 
    # "404", means city is found otherwise, 
    # city is not found 
    if x["cod"] != "404": 

        # store the value of "main" 
        # key in variable y 
        y = x["main"] 

        # store the value corresponding 
        # to the "temp" key of y 
        current_temperature = y["temp"] 

        # store the value corresponding 
        # to the "pressure" key of y 
        current_pressure = y["pressure"] 

        # store the value corresponding 
        # to the "humidity" key of y 
        current_humidiy = y["humidity"] 

        # store the value of "weather" 
        # key in variable z 
        z = x["weather"] 

        # store the value corresponding 
        # to the "description" key at 
        # the 0th index of z 
        weather_description = z[0]["description"] 

        # print following values
        t=str(current_temperature)
        p= str(current_pressure)
        h= str(current_humidiy)
        desc = str(weather_description)

        speak("The weather of the" + city_name + "is")
        print(" Temperature (in kelvin unit) is " + t)
        speak("Temperature (in kelvin unit) is " + t)
        print("atmospheric pressure (in hPa unit) is " + p)
        speak("atmospheric pressure (in hPa unit) is " + p)
        print("humidity (in percentage) is " + h)
        speak("humidity (in percentage) is " + h)
        print("weather condition is " + desc)
        speak("weather condition is" + desc)

        

    else: 
        print(" City Not Found ") 
    


def Boil_milk():
    import cv2, os, time, keras
    import numpy as np
    from keras_retinanet import models
    from keras_retinanet.utils.image import read_image_bgr, preprocess_image, resize_image
    from keras_retinanet.utils.visualization import draw_box, draw_caption
    from keras_retinanet.utils.colors import label_color
    import matplotlib.pyplot as plt
    import numpy as np
    import tensorflow as tf

    class Boil:
        obj_num = 0
        x = 0
        y = 0
        def __init__(self, num, x, y, b):
            self.obj_num = num
            self.x = x
            self.y = y
            self.b = b

    def get_session():
        config = tf.compat.v1.ConfigProto()
        config.gpu_options.allow_growth = True
        return tf.compat.v1.Session(config=config)

    os.system(r"echo '' > C:\Users\sumov\OneDrive\Desktop\Boiling_Milk_Dataset\webcam.txt")
    f = open(r"C:\Users\sumov\OneDrive\Desktop\Boiling_Milk_Dataset\webcam.txt", "a")
    tf.compat.v1.keras.backend.set_session(get_session())
    #model = models.load_model("/home/ringlayer/Desktop/app/retinanet1/models/resnet50_09.h5", backbone_name='resnet50')
    model = models.load_model(r"C:\Users\sumov\OneDrive\Desktop\Boiling_Milk_Dataset\model.h5", backbone_name='resnet50')
    #model = models.convert_model(model)
    print(model.summary())
    labels_to_names = {0: 'Boiled', 1: 'Steaming'}

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)

    while True:
        try:
            current_boil = 0
            box_lists = []
            ret, image = cap.read()
            draw = image.copy()
            draw = cv2.resize(draw,(640,480))
            draw = cv2.cvtColor(draw, cv2.COLOR_BGR2RGB)
            image = preprocess_image(image)
            image, scale = resize_image(image)
            start = time.time()
            boxes, scores, labels = model.predict(np.expand_dims(image, axis=0))

            boxes /= scale

            for box, score, label in zip(boxes[0], scores[0], labels[0]):
                if score < 0.5:
                    break
                current_boil += 1
                color = label_color(label)
                b = box.astype(int)
                x = b[0]
                y = b[1]
                box_lists.append(Boil(current_boil, x, y, b))
                draw_box(draw, b, color=color)
                caption = "{} {:.3f}".format(labels_to_names[label], score)
                draw_caption(draw, b, caption)

            draw = cv2.cvtColor(draw, cv2.COLOR_RGB2BGR)
            cv2.imshow('framename', draw)
            if current_boil > 0:
                #os.system("cls")
                str_data = "\n\n*******Record of Boiling Milk Data*******"
                for obj in box_lists:
                    str_data += "\nMilk Boiled : " + str(obj.obj_num)
                    print(obj.obj_num)
                        #print("The Milk is Boiled")
                    str_data += "\ngot x : " + str(obj.x)
                    str_data += "\ngot y : " + str(obj.y)
                    str_data += "\nfull coordinate : " + str(obj.b)
                    str_data += "\n"
                    decision=str(caption[:4])
                    
                f.write(str_data)
                #print(str_data)
                print(caption)
                if decision =='Boil':
                    result=('Milk is Boiled')
                    
                    speak(result)
                
                #print(box_lists)
            
        except:
            pass

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

    f.close()
    


if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            r = sr.Recognizer()
            speak('Searching Wikipedia...')
            with sr.Microphone() as source:
                r.pause_threshold = 1
                audio = r.listen(source)
                ip = r.recognize_google(audio, language='en-in')
                print(f"User said: {ip}\n")
                query = query.replace("wikipedia", ip)
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
    

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'check boiling milk' in query:
            speak("Checking on the milk")
            Boil_milk()
        elif 'play youtube' in query:
            Youtube()
        elif 'close youtube' in query:
            player.stop()
        elif 'check weather' in query:
            weather()
        elif 'quarantine' in query:
            speak("nothing different from what you did for past 21 years")
        elif 'search google' in query:
            speak("Searching google")
            google_search()
        elif 'close browser' in query:
            os.system("taskkill/im chrome.exe")
        elif 'dictionary' in query:
            speak("Opening Dictionary")
            open_dictionary()
        elif 'voices' in query:
            speak("Enemies Ahead!!")
            speak("fall back to safe zone")
            speak("There can only be one winner, lets go")
            speak("marked a location")
            speak("May Raa  game lag hoe raa haa hae")