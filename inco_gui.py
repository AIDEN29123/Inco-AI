import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
import ecapture as ec
import wolframalpha
import json
import requests
import pyjokes
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import time
import clipboard

tk = Tk()
tk.title('Message Encrypter/Decrypter 1')

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def Encrypt():
    passwd = entry1.get()
    passwd_s = "" # 암호화한 비밀번호 저장
    passwd2 = "" # 복호화한 암호, 첫번째 비밀번호랑 같은지 확인할 것.
    c = '' # 문자 하나 따오기
    ac = 0 # ASCII code 로 변환
    for i in range(len(passwd)) :
        c = passwd[i]   # 개별 문자
        ac = ord(c)     # 개별 문자의 아스키 코드
        ac += 2         # 개별 아스키 코드 값 2 증가
        c = chr(ac)     # 아스키 코드를 문자로 변환
        passwd_s += c   # 변환된(암호화 한) 암호 저장
    entry2.delete(0,"end")
    entry2.insert(0, passwd_s)

def Copy():
    clipboard.copy(entry2.get())

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        IncoHelloTime.configure(text = "Good Morning")
        speak("Good Morning")
    elif hour>=12 and hour<18:
        IncoHelloTime.configure(text = "Good Afternoon")
        speak("Good Afternoon")
    else:
        IncoHelloTime.configure(text = "Good Evening")
        speak("Good Evening")
    commands()

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-US')
            usersay.configure(f"user said:{statement}\n")

        except Exception as e:
            speak("Sorry, i didn't understand")
            return "None"
        return statement

def startInco():
    speak("Hello, I am your personal assistant, Inco.")
    wishMe()


label0 = Label(tk,text='Speaking')
label0.grid(row=0, column=0)
label1 = Label(tk,text='Inco: ').grid(row=1, column=0)
IncoHello = Label(tk,text='Hello, I am your personal assistant, Inco.')
IncoHello.grid(row=2, column=0)
IncoHelloTime = Label(tk,text='...')
IncoHelloTime.grid(row=3, column=0)
sayInco = Label(tk,text='')
sayInco.grid(row=4,column=0)
usersay = Label(tk,text='')
usersay.grid(row=5,column=0)

btnstartinco = Button(tk,text='Start AI',bg='black',fg='white',command=startInco).grid(row=4,column=1)

# 각 단위 입력받는 부분 만들기
entry1 = Entry(tk)
entry2 = Entry(tk)

btncopy01 = Button(tk, text='Copy',bg='black',fg='white',command=Copy).grid(row=2, column=2)

entry1.grid(row=1,column=1)
entry2.grid(row=2,column=1)

def commands():
    label0.configure(text='Listening')
    sayInco.configure(text='How can I help you ?')
    speak("How can I help you?")
    statement = takeCommand().lower()
    if statement==0:
        label0.configure(text='Listening')

    if "good bye" in statement or "ok bye" in statement or "stop" in statement or "staff" in statement or "okay bye" in statement:
        label0.configure(text='Exiting')
        speak('your personal assistant Inco is shutting down, Good bye')
        sayInco.configure(text = 'Your personal assistant Inco is shutting down, Good bye')



    if 'wikipedia' in statement:
        label0.configure(text='Searching')
        speak('Searching Wikipedia...')
        statement =statement.replace("wikipedia", "")
        results = wikipedia.summary(statement, sentences=3)
        speak("According to Wikipedia")
        sayInco.configure(text = results)
        speak(results)

    elif 'open youtube' in statement:
        label0.configure(text='Opening')
        webbrowser.open_new_tab("https://www.youtube.com")
        speak("youtube is opened on your browser")
        sayInco.configure(text = "Youtube is opened on your browser")
        time.sleep(3)

    elif 'open google' in statement:
        webbrowser.open_new_tab("https://www.google.com")
        speak("Google is open on your broswer")
        sayInco.configure(text = "Google is opened on your browser")
        time.sleep(3)

    elif 'open gmail' in statement:
        webbrowser.open_new_tab("https://mail.google.com")
        speak("Google Mail is opened on your browser")
        sayInco.configure(text = "Google Mail is opened on your browser")
        time.sleep(3)

    elif 'open document from google' in statement:
        webbrowser.open_new_tab("https://docs.google.com")
        speak("Google document is opened on your browser")
        sayInco.configure(text = "Google document is opened on your browser")
        time.sleep(3)

    elif 'open netflix' in statement:
        webbrowser.open_new_tab("https://www.netflix.com")
        speak("Netflix is opened on your browser")
        sayInco.configure(text = "Netflix is opened on your browser")
        time.sleep(3)

    elif 'open naver' in statement:
        webbrowser.open_new_tab("https://www.naver.com")
        speak("Netflix is opened on your browser")
        sayInco.configure(text = "Naver is opened on your browser")
        time.sleep(3)

    elif "weather" in statement:
        api_key="8ef61edcf1c576d65d836254e11ea420"
        base_url="https://api.openweathermap.org/data/2.5/weather?"
        speak("whats the city name")
        sayInco.configure(text = "Whats the city name")
        city_name=takeCommand()
        complete_url=base_url+"appid="+api_key+"&q="+city_name
        response = requests.get(complete_url)
        x=response.json()
        if x["cod"]!="404":
            y=x["main"]
            current_temperature = y["temp"]
            current_humidiy = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            speak(" Temperature in kelvin unit is " +
                    str(current_temperature) +
                    "\n humidity in percentage is " +
                    str(current_humidiy) +
                    "\n description  " +
                    str(weather_description))
            sayInco.configure(text = " Temperature in kelvin unit = " +
                    str(current_temperature) +
                    "\n humidity (in percentage) = " +
                    str(current_humidiy) +
                    "\n description = " +
                    str(weather_description))

        else:
            speak(" City Not Found ")
            sayInco.configure(text = " City Not Found ")



    elif 'time' in statement:
        strTime=datetime.datetime.now().strftime("%I:%M %p")
        speak(f"the time is {strTime}")
        sayInco.configure(text = f"the time is {strTime}")

    elif 'who are you' in statement or 'what can you do' in statement:
        speak('I am Inco version 1 point O your, persoanl assistant.')
        sayInco.configure(text = 'I am Inco version 1.0 your, persoanl assistant.')

    elif 'what can you do' in statement:
        speak('opening youtube,google chrome,gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather' 
        'in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!')
        sayInco.configure(text = 'opening youtube,google chrome,gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather'
        'in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!')


    elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
        speak("I was built by Dopics")
        sayInco.configure(text = "I was built by Dopics")

    elif "version" in statement:
        speak("Current version of Inco you are using is alpha 1 point 0")
        sayInco.configure(text = "Current version of Inco you are using is alpha 1.0")

    elif "open stackoverflow" in statement:
        webbrowser.open_new_tab("https://stackoverflow.com/login")
        speak("Here is stackoverflow")
        sayInco.configure(text = "Stackoverflow is opened on your browser")

    elif 'news' in statement:
        news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
        speak('Here are some headlines from the Times of India,Happy reading')
        sayInco.configure(text = 'Here are some headlines from the Times of India,Happy reading')
        time.sleep(6)

    elif "camera" in statement or "take a photo" in statement:
        ec.capture(0,"robo camera","img.jpg")

    elif 'search'  in statement:
        statement = statement.replace("search ", "")
        webbrowser.open_new_tab("https://www.google.com.hk/search?q="+statement)
        time.sleep(5)

    elif 'ask' in statement:
        speak('I can answer to computational and geographical questions and what question do you want to ask now')
        question=takeCommand()
        app_id="WJYHUL-XG3KJP4K67"
        client = wolframalpha.Client('WJYHUL-XG3KJP4K67')
        res = client.query(question)
        answer = next(res.results).text
        speak(answer)
        sayInco.configure(text = answer)

    elif 'joke' in statement:
        speak(pyjokes.get_joke())
        sayInco.configure(text = pyjokes.get_joke())

    else:
        speak("please say it again.")
        sayInco.configure(text = "Please say it again.")


        #elif "log off" in statement or "sign out" in statement:
            #speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            #subprocess.call(["shutdown", "/l"])

time.sleep(3)







tk.mainloop()