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
import smtplib
import subprocess
import pyaudio

print('Hello, I am your personal assistant, Inco.')

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Good Morning")
        print("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
        print("Good Afternoon")
    else:
        speak("Good Evening")
        print("Good Evening")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-US')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Sorry, i didn't understand")
            return "None"
        return statement

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    yourgoogleemail = input("Please enter your gmail: ")
    yourgooglepassword = input("Please enter your google password: ")
    server.login(yourgoogleemail, yourgooglepassword)
    server.sendmail(yourgoogleemail, to, content)
    server.close

speak("Hello, I am your personal assistant, Inco.")
wishMe()


if __name__=='__main__':


    while True:
        speak("How can I help you?")
        statement = takeCommand().lower()
        if statement==0:
            continue

        if "good bye" in statement or "ok bye" in statement or "stop" in statement or "goodbye" in statement or "okay bye" in statement or "shut down" in statement or "deactivate" in statement:
            speak('Your personal assistant Inco is shutting down, Good bye')
            print('Your personal assistant Inco is shutting down, Good bye')
            break



        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is opened on your browser")
            print("Youtube is opened on your browser")
            time.sleep(3)

        elif 'search' in statement and 'in Google Image' in statement:
            statement = statement.replace("search ", "")
            statement = statement.replace(" in Google Image", "")
            webbrowser.open_new_tab("https://www.google.com.hk/search?q="+statement)
            speak("These are the results on Goole Image")
            print("These are the results on Goole Image")
            time.sleep(3)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google is opened on your broswer")
            print("Google is opened on your broswer")
            time.sleep(3)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("https://mail.google.com")
            speak("Google Mail is opened on your browser")
            print("Google Mail is opened on your browser")
            time.sleep(3)

        elif 'open document from google' in statement or 'open document in google' in statement:
            webbrowser.open_new_tab("https://docs.google.com")
            speak("Google document is opened on your browser")
            print("Google document is opened on your browser")
            time.sleep(3)

        elif 'open netflix' in statement:
            webbrowser.open_new_tab("https://www.netflix.com")
            speak("Netflix is opened on your browser")
            print("Netflix is opened on your browser")
            time.sleep(3)

        elif 'open naver' in statement:
            webbrowser.open_new_tab("https://www.naver.com")
            speak("Naver is opened on your browser")
            print("Naver is opened on your browser")
            time.sleep(3)

        elif 'open baidu' in statement:
            webbrowser.open_new_tab("https://www.baidu.com")
            speak("Baidu is opened on your browser")
            print("Baidu is opened on your browser")
            time.sleep(3)

        elif 'open discord' in statement:
            webbrowser.open_new_tab("https://www.discord.com")
            speak("Discord is opened on your browser")
            print("Discord is opened on your browser")
            time.sleep(3)

        elif 'open github' in statement:
            webbrowser.open_new_tab("https://www.github.com")
            speak("Github is opened on your browser")
            print("Github is opened on your browser")
            time.sleep(3)

        elif 'open facebook' in statement:
            webbrowser.open_new_tab("https://www.facebook.com")
            speak("Facebook is opened on your browser")
            print("Facebook is opened on your browser")
            time.sleep(3)

        elif 'open twitter' in statement:
            webbrowser.open_new_tab("https://www.twitter.com")
            speak("Twitter is opened on your browser")
            print("Twitter is opened on your browser")
            time.sleep(3)

        elif 'open instagram' in statement:
            webbrowser.open_new_tab("https://www.instagram.com")
            speak("Instagram is opened on your browser")
            print("Instagram is opened on your browser")
            time.sleep(3)

        elif 'open wikipedia' in statement:
            webbrowser.open_new_tab("https://www.wikipedia.org")
            speak("Wikipedia is opened on your browser")
            print("Wikipedia is opened on your browser")
            time.sleep(3)

        elif 'open yandex' in statement:
            webbrowser.open_new_tab("https://www.yandex.ru")
            speak("Yandex is opened on your browser")
            print("Yandex is opened on your browser")
            time.sleep(3)

        elif 'open yahoo' in statement:
            webbrowser.open_new_tab("https://www.yahoo.com")
            speak("Yahoo is opened on your browser")
            print("Yahoo is opened on your browser")
            time.sleep(3)

        elif 'open whatsapp' in statement:
            webbrowser.open_new_tab("https://www.whatsapp.com")
            speak("WhatsApp is opened on your browser")
            print("WhatsApp is opened on your browser")
            time.sleep(3)

        elif 'open amazon' in statement:
            webbrowser.open_new_tab("https://www.amazon.com")
            speak("Amazon is opened on your browser")
            print("Amazon is opened on your browser")
            time.sleep(3)

        elif 'open live connect' in statement:
            webbrowser.open_new_tab("https://www.live.com")
            speak("Live Connect is opened on your browser")
            print("Live Connect is opened on your browser")
            time.sleep(3)

        elif 'open zoom' in statement:
            webbrowser.open_new_tab("https://www.zoom.com")
            speak("Zoom is opened on your browser")
            print("Zoom is opened on your browser")
            time.sleep(3)

        elif 'open spotify' in statement:
            webbrowser.open_new_tab("https://www.spotify.com")
            speak("Spotify is opened on your browser")
            print("Spotify is opened on your browser")
            time.sleep(3)

        elif 'open skype' in statement:
            webbrowser.open_new_tab("https://www.skype.com")
            speak("Skype is opened on your browser")
            print("Skype is opened on your browser")
            time.sleep(3)

        elif 'open snapchat' in statement:
            webbrowser.open_new_tab("https://www.snapchat.com")
            speak("Snapchat is opened on your browser")
            print("Snapchat is opened on your browser")
            time.sleep(3)

        elif 'open linkedin' in statement:
            webbrowser.open_new_tab("https://www.linkedin.com")
            speak("Linkedin is opened on your browser")
            print("Linkedin is opened on your browser")
            time.sleep(3)

        elif 'open pinterest' in statement:
            webbrowser.open_new_tab("https://www.pinterest.com")
            speak("Pinterest is opened on your browser")
            print("Pinterest is opened on your browser")
            time.sleep(3)

        elif 'open quora' in statement:
            webbrowser.open_new_tab("https://www.quora.com")
            speak("Quora is opened on your browser")
            print("Quora is opened on your browser")
            time.sleep(3)

        elif 'open tiktok' in statement:
            webbrowser.open_new_tab("https://www.tiktok.com")
            speak("TikTok is opened on your browser")
            print("TikTok is opened on your browser")
            time.sleep(3)

        elif 'open flickr' in statement:
            webbrowser.open_new_tab("https://www.flickr.com")
            speak("Flickr is opened on your browser")
            print("Flickr is opened on your browser")
            time.sleep(3)

        elif 'open microsoft office' in statement:
            webbrowser.open_new_tab("https://www.office.com")
            speak("Microsoft Office is opened on your browser")
            print("Microsoft Office is opened on your browser")
            time.sleep(3)

        elif 'open reddit' in statement:
            webbrowser.open_new_tab("https://www.reddit.com")
            speak("Reddit is opened on your browser")
            print("Reddit is opened on your browser")
            time.sleep(3)

        elif 'open vk' in statement:
            webbrowser.open_new_tab("https://www.vk.com")
            speak("VK is opened on your browser")
            print("VK is opened on your browser")
            time.sleep(3)

        elif 'open twitch' in statement:
            webbrowser.open_new_tab("https://www.twitch.tv")
            speak("Twitch is opened on your browser")
            print("Twitch is opened on your browser")
            time.sleep(3)

        elif 'open bing' in statement:
            webbrowser.open_new_tab("https://www.bing.com")
            speak("Bing is opened on your browser")
            print("Bing is opened on your browser")
            time.sleep(3)

        elif 'open bilibili' in statement:
            webbrowser.open_new_tab("https://www.bilibili.com")
            speak("Bilibili is opened on your browser")
            print("Bilibili is opened on your browser")
            time.sleep(3)

        elif 'open mail.ru' in statement:
            webbrowser.open_new_tab("https://www.mail.ru")
            speak("Mail dot Ru is opened on your browser")
            print("Mail.Ru is opened on your browser")
            time.sleep(3)

        elif 'open duckduckgo' in statement:
            webbrowser.open_new_tab("https://www.duckduckgo.com")
            speak("DuckDuckGo is opened on your browser")
            print("DuckDuckGo is opened on your browser")
            time.sleep(3)

        elif 'open roblox' in statement:
            webbrowser.open_new_tab("https://www.roblox.com")
            speak("Roblox is opened on your browser")
            print("Roblox is opened on your browser")
            time.sleep(3)

        elif 'open microsoft online' in statement:
            webbrowser.open_new_tab("https://www.microsoftonline.com")
            speak("Microsoft Online is opened on your browser")
            print("Microsoft Online is opened on your browser")
            time.sleep(3)

        elif 'open microsoft' in statement:
            webbrowser.open_new_tab("https://www.microsoft.com")
            speak("Microsoft is opened on your browser")
            print("Microsoft is opened on your browser")
            time.sleep(3)

        elif 'open samsung' in statement:
            webbrowser.open_new_tab("https://www.samsung.com")
            speak("Samsung is opened on your browser")
            print("Samsung is opened on your browser")
            time.sleep(3)

        elif 'open qq' in statement:
            webbrowser.open_new_tab("https://www.qq.com")
            speak("QQ is opened on your browser")
            print("QQ is opened on your browser")
            time.sleep(3)

        elif 'open document from qq' in statement or 'open document in qq' in statement:
            webbrowser.open_new_tab('https://docs.qq.com')
            speak("QQ document is opened on your browser")
            print("QQ document is opened on your browser")
            time.sleep(3)

        elif 'open msn' in statement:
            webbrowser.open_new_tab("https://www.msn.com")
            speak("MSN is opened on your browser")
            print("MSN is opened on your browser")
            time.sleep(3)

        elif 'open docomo' in statement:
            webbrowser.open_new_tab("https://www.docomo.ne.jp")
            speak("Docomo is opened on your browser")
            print("Docomo is opened on your browser")
            time.sleep(3)

        elif 'open yahoo news' in statement:
            webbrowser.open_new_tab("https://news.yahoo.co.jp")
            speak("Yahoo News is opened on your browser")
            print("Yahoo News is opened on your browser")
            time.sleep(3)

        elif 'open globo' in statement:
            webbrowser.open_new_tab("https://www.globo.com")
            speak("Globo is opened on your browser")
            print("Globo is opened on your browser")
            time.sleep(3)

        elif 'open telegram' in statement:
            webbrowser.open_new_tab("https://www.t.me")
            speak("Telegram is opened on your browser")
            print("Telegram is opened on your browser")
            time.sleep(3)

        elif 'open ebay' in statement:
            webbrowser.open_new_tab("https://www.ebay.com")
            speak("eBay is opened on your browser")
            print("eBay is opened on your browser")
            time.sleep(3)

        elif 'open bbc' in statement:
            webbrowser.open_new_tab("https://www.bbc.co.uk")
            speak("BBC is opened on your browser")
            print("BBC is opened on your browser")
            time.sleep(3)

        elif 'open daum' in statement:
            webbrowser.open_new_tab("https://www.daum.net")
            speak("Daum is opened on your browser")
            print("Daum is opened on your browser")
            time.sleep(3)

        elif 'open calculator' in statement:
            subprocess.Popen('C:\\Windows\\System32\\calc.exe')
            speak("Calculator is opened.")
            print("Calculator is opened.")
            time.sleep(3)

        elif 'open notepad' in statement:
            subprocess.Popen('C:\\Windows\\System32\\notepad.exe')
            speak("Notepad is opened.")
            print("Notepad is opened.")
            time.sleep(3)

        elif 'open wordpad' in statement:
            subprocess.Popen('C:\\Windows\\System32\\write.exe')
            speak("Wordpad is opened.")
            print("Wordpad is opened.")
            time.sleep(3)

        elif 'open file explorer' in statement:
            os.popen('explorer.exe')
            speak("File explorer is opened.")
            print("File explorer is opened.")
            time.sleep(3)

        elif 'who is' in statement:
            person = statement.replace('who is', '')
            info = wikipedia.summary(person, 1)
            print(info)
            speak(info)

        elif 'what is' in statement:
            person = statement.replace('what is', '')
            info = wikipedia.summary(person, 1)
            print(info)
            speak(info)

        elif 'calculate' in statement:
            speak("What is the first number?")
            print("What is the first number?")
            num1=takeCommand()
            speak("First number inputed")
            print("First number inputed"+num1)
            speak("What operation would you like to use?")
            print("What operation would you like to use?")
            op=takeCommand()
            speak("Operation inputed")
            print("Operation inputed"+op)
            speak("What is the second number?")
            print("What is the second number?")
            num2=takeCommand()
            speak("Second number inputed")
            print("Second number inputed"+num2)
            if op == "Plus":
                speak(num1 + num2)
                print(num1 + num2)
            elif op == "Substract":
                speak(num1 - num2)
                print(num1 - num2)
            elif op == "Times":
                speak(num1 * num1)
                print(num1 * num2)
            elif op == "Divided by":
                speak(num1 / num2)
                print(num1 / num2)
            else:
                speak("Invalid operator")
                print("Invalid operator")





        elif "weather" in statement:
            api_key="8ef61edcf1c576d65d836254e11ea420"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            print("whats the city name")
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
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" City Not Found ")



        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%I:%M %p")
            speak(f"the time is {strTime}")
            print(f"the time is {strTime}")

        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am Inco version 1 point O your, persoanl assistant.')
            print('I am Inco version 1.0 your, persoanl assistant.')

        elif 'what can you do' in statement:
            speak('opening youtube,google chrome,gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather'
            'in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!')
            print('opening youtube,google chrome,gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather'
            'in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!')


        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Dopics")
            print("I was built by Dopics")

        elif "version" in statement:
            speak("Current version of Inco you are using is alpha 1 point 0")
            print("Current version of Inco you are using is alpha 1.0")

        elif "open stackoverflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Here is stackoverflow")
            print("Here is stackoverflow")

        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            print('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)

        elif "camera" in statement or "take a photo" in statement:
            ec.capture(0,"robo camera","img.jpg")

        elif 'search' in statement:
            statement = statement.replace("search ", "")
            webbrowser.open_new_tab("https://www.google.com.hk/search?q="+statement)
            speak("Here are some results for "+statement)
            print("Here are some results for "+statement)
            time.sleep(5)

        elif 'say' in statement:
            statement = statement.replace("say ", "")
            speak(statement)
            print(statement)
            time.sleep(5)

        elif 'ask' in statement:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            question=takeCommand()
            app_id="WJYHUL-XG3KJP4K67"
            client = wolframalpha.Client('WJYHUL-XG3KJP4K67')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)

        elif 'joke' in statement:
            speak(pyjokes.get_joke())
            print(pyjokes.get_joke())

        elif 'hello' in statement:
            speak("Hello, nice to meet you.")
            print("Hello, nice to meet you.")
            time.sleep(1)

        elif 'how are you' in statement:
            speak("I feel good today.")
            print("I feel good today.")
            time.sleep(1)

        elif 'what are you doing now' in statement:
            speak("I'm watching Avengers with my popcorn next to me.")
            print("I'm watching Avengers with my popcorn next to me.")
            time.sleep(1)

        elif 'how old are you' in statement or 'what age are you' in statement:
            speak("Emmm... Not even 1 I think.")
            print("Emmm... Not even 1 I think.")
            time.sleep(1)

        elif 'you are smart' in statement or "you're smart" in statement:
            speak("Thank you very much.")
            print("Thank you very much.")
            time.sleep(1)

        elif "what's your name" in statement or "what is your name" in statement:
            speak("My name is Inco. Nice to meet you.")
            print("My name is Inco. Nice to meet you.")
            time.sleep(1)

        elif 'email' in statement:
            try:
                sendtoemail = input("Who will you send the email to?")
                speak("Who will you send the email to?")
                print("Who will you send the email to?")
                speak("What should I say?")
                print("What should I say?")
                content = takeCommand()
                to = sendtoemail
                sendEmail(to, content)
                speak("Email has been sent!")
                print("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to send this email")

        else:
            speak("please say it again.")
            print("Please say it again.")


        #elif "log off" in statement or "sign out" in statement:
            #speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            #subprocess.call(["shutdown", "/l"])

time.sleep(3)
