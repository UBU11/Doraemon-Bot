import os
import sys
import webbrowser
import pyttsx3
import speech_recognition as sr
import datetime
import pyautogui


def initialize():
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    rate = engine.getProperty("rate")
    engine.setProperty("rate", rate - 50)
    engine.getProperty("volume")
    engine.setProperty("volume", 0.25)
    return engine

def speak(text):
    engine = initialize()
    engine.say(text)
    engine.runAndWait()

def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        print("Listening.......")
        r.pause_threshold = 1
        r.phrase_threshold = 0.3
        r.sample_rate = 48000
        r.dynamic_energy_threshold = True
        r.operation_timeout = 5
        r.non_speaking_duration = 0.5
        r.dynamic_energy_adjustment_damping = 2
        r.energy_threshold = 4000
        r.phrase_time_limit = 10
        # print(sr.Microphone.list_microphone_names())
        audio = r.listen(source)
    try:
       print("\r", end="", flush=True)
       print("Recognizing....", end="", flush=True)
       query =  r.recognize_google(audio, language='en-in')
       print(f"User said: {query}\n")
    except Exception as e:
        print("say that again please")
        return "None"
    return query

def cal_day():
    day = datetime.datetime.today().weekday() + 1
    day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}
    if day in day_dict.keys():
        day_of_week = day_dict[day]
        print(day_of_week)
    return day_of_week

def wishMe():
    
    hour = int(datetime.datetime.now().hour)
    t = datetime.datetime.now().strftime("%I:%M %p")
    day = cal_day()
    if(hour >= 0 and hour < 12 and ("AM" in t)):
        speak(f"Good Morning Bruh, it's {t} and today is {day}")
    elif(hour >= 12 and hour < 18 and ("PM" in t)):
        speak(f"Good Afternoon Bruh, it's {t} and today is {day}")
    elif(hour >= 18 and hour < 24 and ("PM" in t)):
        speak(f"Good Evening Bruh, it's {t} and today is {day}")
    else:
        speak(f"Good Night Bruh, it's {t} and today is {day}")

def social_media(command):
    if 'facebook' in command:
     speak("Opening your facebook")
     webbrowser.open("https://www.facebook.com")
    elif 'discord' in command:
     speak("Opening your discord")
     webbrowser.open("https://discord.com")
    elif 'whatsapp' in command:
     speak("Opening your whatsapp")
     webbrowser.open("https://web.whatsapp.com")
    elif 'instagram' in command:
     speak("Opening your instagram")
     webbrowser.open("https://www.instagram.com")
    elif 'twitter' in command:
     speak("Opening your twitter")
     webbrowser.open("https://twitter.com")
    elif 'linkedin' in command:
     speak("Opening your linkedin")
     webbrowser.open("https://www.linkedin.com")
    elif 'youtube' in command:
     speak("Opening your youtube")
     webbrowser.open("https://www.youtube.com")
    elif 'reddit' in command:
        speak("Opening your reddit")
        webbrowser.open("https://www.reddit.com")
    elif 'google' in command:
        speak("Opening your google")
        webbrowser.open("https://www.google.com")

def schedule():
   day = cal_day()
   speak("bruh today's schedule is")
   week = {
     "Monday": "Bruh, from 4:00 am to 6:30 am, you have to learn backend in-depth.",
    "Tuesday": "Bruh, from 4:00 am to 6:30 am, you need to conduct the Tinkerhub event.",
    "Wednesday": "Bruh, from 4:00 am to 6:30 am, focus on AI and machine learning concepts.",
    "Thursday": "Bruh, from 4:00 am to 6:30 am, work on your college-specific Flutter app with Firebase.",
    "Friday": "Bruh, from 4:00 am to 6:30 am, practice data structures and algorithms for hackathons.",
    "Saturday": "Bruh, from 4:00 am to 6:30 am, study psychology and read self-improvement books.",
    "Sunday": "Bruh, from 4:00 am to 6:30 am, plan the upcoming week and do project debugging/refinement."
   }
   if day in week.keys():
      speak(week[day])
def openApp(command):
   if "calculator" in command:
      speak("opening the Calculator")
      os.startfile('c:\\Windows\\System32\\calc.exe')
   elif "notepad" in command:
      speak("opening the notepad")
      os.startfile('c:\\Windows\\System32\\notepad.exe')
   
if __name__ == "__main__":
    wishMe()
    while True:
        # query = command().lower()
        # print(query)
        query = input("Enter your command: ")
        if ("facebook" in query or "discord" in query or "whatsapp" in query or "instagram" in query or "twitter" in query or "linkedin" in query or "youtube" in query or "reddit" in query or "google" in query):
            social_media(query)
        elif ("University time table" in  query or ("schedule" in query)):
           schedule()
        elif("Volume up" in query or "increase volume" in query):
           pyautogui.press("volumeup")
           speak("volume increased")
        elif("Volume down" in query or "decrease volume" in query):
           pyautogui.press("volumedown")
           speak("volume decreased")
        elif("volume mute" in query or "mute the sound" in query):
            pyautogui.press("volumemute")
            speak("volume muted")
        elif("open calculator" in query or "open notepad" in query):
           openApp(query)
        elif 'exit' in query:
           sys.exit()
    

