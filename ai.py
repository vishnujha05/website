import pyttsx3
import win32com
import win32api
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import sys
import datetime


engine = pyttsx3.init ('sapi5')
voices = engine.getProperty ('voices')
engine.setProperty('voice' , voices[0].id )
print(voices[1].id)
def speak (audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12 :
        speak("good morning sir!")
    elif hour>=12 and hour<18:
        speak("good afternoon sir!")
    else:
        speak("gd night sir!")
    speak("hello sir! i am your assistance. please tell me how may i help you ")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
            
    try:
        print("recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query}\n")

    except Exception as e:
          #print(e)
          print("say that again please....")
          return "none"
    return query



if __name__ == "__main__":
    #speak ("i am vishnu")
    wishMe()
    while true :
        query = takecommand().lower()
        if 'wikipedia' in query:
            speak('searching wikipedia....')
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            print(result)
            speak(result)
        elif 'open youtube' in query :
            webbrowser.open("youtube.com")
        elif 'open google' in query :
            webbrowser.open("google.com")
        elif 'open stack overflow' in query :
            webbrowser.open("stackoverflow.com")
        #elif 'play music' in query :
        elif 'what time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the is {strtime}")
        
            


        

        
        
            


