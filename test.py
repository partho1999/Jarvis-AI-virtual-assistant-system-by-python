import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)





def speak(audio):
 engine.say(audio)
 engine.runAndWait()

if __name__ == "__main__":
 speak("sir! please inter the pasword")
 
password=input("enter the pssword:")
if password=='section101':

 import pyttsx3 #pip install pyttsx3
 import speech_recognition as sr #pip install speechRecognition
 import datetime  #pip install datetime
 import wikipedia #pip install wikipedia
 import webbrowser #pip install webbrowser
 import os
 import time
 import sys 
 import pyowm #pip install pyowm


 engine = pyttsx3.init('sapi5')
 voices = engine.getProperty('voices')
 #print(voices[0].id)
 engine.setProperty('voice',voices[0].id)




 def speak(audio):
   engine.say(audio)
   engine.runAndWait()

 def wishMe():
   hour = int(datetime.datetime.now().hour)
   if hour>=4 and hour<12:
      speak("Good morning...!")

   elif hour>=12 and hour<18:  
     speak("good afternoon...!")

   else:
     speak("good evening...!")  
    
   speak("Hello sir...! i am jarvis  please tell me how may i help you")

 def takeCommand():
  r = sr.Recognizer()
  with sr.Microphone() as source:
    print("listening...")
    r.pause_threshold =1
    audio = r.listen(source)

  try:
    print("recognizing...")
    query = r.recognize_google(audio,language='en-in')
    print(f"you said:{query}\n")

  except Exception as e:
     #print(e)
     print("sorry sir! i can't recognize please say that again....")
     return "None"
  
  return query
  
  

 if __name__ == "__main__":
  wishMe()
  
  while True:
  
    query = takeCommand().lower()

    if 'wikipedia'in query:
     speak('searching wikipedia....')
     query = query.replace("wikipedia","")
     results = wikipedia.summary(query,sentences=5)
     speak("According to wikipedia")
     print(results)
     speak(results)

    elif 'open youtube'in query:
      webbrowser.open("https://www.youtube.com/")
      speak('opening youtube...')
    
    elif 'open google'in query:
      webbrowser.open("https://www.google.com/")
      speak('opening google...')

    elif 'open facebook'in query:
      webbrowser.open("https://www.facebook.com/")
      speak('opening facebook...')
    
    elif 'open mail'in query:
      webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
      speak('opening mail inbox...')
    
    elif 'open whatsapp'in query:
      webbrowser.open("https://web.whatsapp.com/")
      speak('opening whats app...')
    
    elif 'open instagram'in query:
      webbrowser.open("https://www.instagram.com/")
      speak('opening instagram...')

    elif 'time' in query:
      strTime = datetime.datetime.now().strftime("%H:%M:%S")
      speak(f"sir, the time is {strTime}, ")
      print(strTime) 
    
    elif 'date' in query:
      tday = datetime.date.today()
      speak(f"sir, the date is {tday.day}, ")
      print(tday.day) 

    elif 'month' in query:
      tday = datetime.date.today()
      speak(f"sir, the month is {tday.month}, ")
      print(tday.month) 

    elif 'about you' in query or 'introduce' in query:
      speak("sir! i'm jarvis, i'm your private assistant, i always try to help you")
    
    elif 'sleep' in query or 'break' in query:
     speak("ok sir initiating sleeping mode for five minutes")
     time.sleep(300)

    elif 'search google' in query or 'search in google' in query or 'searching' in query:
     r =sr.Recognizer()
     with sr.Microphone() as source:
       speak("sir what i have  to search...!")
       print("listening...")
       r.pause_threshold = 2
       audio = r.listen(source)
       speak("ok sir! searching")

     try:
       print("Recognizing....") 
       text = r.recognize_google(audio,language='en-in')
       print("you said:".format(text))
       url='https://www.google.co.in/search?sxsrf=ACYBGNRevpqwB1xnD7JY-2FquUNSb_FcSg%3A1576600715964&source=hp&ei=iwT5XcfOOJzZz7sPq7aCgAU&q=' 
       search_url=url+text
       webbrowser.open(search_url)

     except Exception as e:
       # print(e)
       print("sorry sir..i can't understand say that again plz...!")

    elif 'website' in query:
     r =sr.Recognizer()
     with sr.Microphone() as source:
       speak("sir which website i have to  search...!")
       print("sir  searching...!")
       r.pause_threshold = 2
       audio = r.listen(source)

     try:
       print("Recognizing....") 
       text = r.recognize_google(audio,language='en-in')
       print("you said:".format(text))
       webbrowser.open(text)

     except Exception as e:
        # print(e)
        print("sorry sir..i can't understand say that again plz...!")

    elif 'music' in query or 'song' in query:
      music_dir = 'E:\\video'
      video = os.listdir(music_dir)
      print(video)
      os.startfile(os.path.join(music_dir, video[0]))


    elif 'quit' in query:
      speak("ok sir switching quit mode, thanks for your time")
      sys.exit()

    elif 'shutdown' in query:
      speak("ok sir! initiating the shutdown process...!")
      speak("sir! i will also offline with this process...! thanks for your time...!")
      os.system("shutdown /s /t 20")

    elif 'restart' in query:
      speak("ok sir! initiating the restart process...!")
      speak("sir! i will also offline with this process...! thanks for your time...!")
      os.system("shutdown /r /t 20")
    
    elif 'sign out' in query:
      speak("ok sir! initiating the sign out process...!")
      speak("sir! i will also offline with this process...! thanks for your time...!")
      os.system("shutdown /l ")
      
    elif 'are you there' in query:
      speak("yes sir...! always at your service")

    elif 'thanks' in query or 'thank you' in query:
      speak("you are most welcome sir! everything for you...!")
      
    elif 'open code' in query or 'project file' in query or 'open vs code' in query:
      codePath="C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
      speak("opening code...!")
      os.startfile(codePath)

    elif 'open a new tab' in query or 'browser' in query or 'open chrome' in query:
      codePath="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
      speak("opening chrome...!")
      os.startfile(codePath)

    #elif 'motherf*****' in query or 'asshole' in query or 'bainchoad' in query:
      #speak("sir...!gentelman doesn't talk this way...!")
      

    elif'how are you' in query:
     hour = int(datetime.datetime.now().hour)
     if hour>=5 and hour<10:
       speak(" sir! i'm always fine...!")

     else:
       speak(" sir! i'm always fine...! how was your day...!")
       
      

    elif 'weather' in query or 'temperature' in query :
     degree_sign=u'\N{DEGREE SIGN}'
     owm=pyowm.OWM('a8401ab41d6d7db45008c61f4d8eae63')
     observation=owm.weather_at_place('kolkata,in')
     weather=observation.get_weather()
     temperature=weather.get_temperature('celsius')['temp']
     wind=weather.get_wind('miles_hour')['speed']
     status=weather.get_detailed_status()

     speak(f'sir! the temperature is today  {temperature}{degree_sign} celsius...!')
     print(f'the temperature is today = {temperature}{degree_sign}')
     speak(f' the wind speed is today  {wind} miles per hour...!')
     print(f'the wind speed is today = {wind} m/h..!')
     speak(f' the weather status today is  {status}...!')
     print(f'the weather status today is = {status}')

    elif 'close chrome' in query or'close the browser' in query:
     speak("closing chrome....")
     os.system('TASKKILL /F /IM chrome.exe') 

    elif 'close code' in query or 'close vs code' in query:
      speak("closing code....")
      os.system('TASKKILL /F /IM Code.exe')

else:
  speak("sorry you can't inter this system you are not my boss...!")
  print("sorry you can't inter this system you are not my boss...!")
  speak("by the way what's name?")
  print("by the way what's name?")

def takeCommand():
  r = sr.Recognizer()
  with sr.Microphone() as source:
    print("listening...")
    r.pause_threshold =1
    audio = r.listen(source)

  try:
    print("recognizing...")
    query = r.recognize_google(audio,language='en-in')
    print(f"you said:{query}\n")

  except Exception as e:
     #print(e)
     print("sorry sir! i can't recognize please say that again....")
     return "None"
  
  return query

query = takeCommand().lower()

speak('nice to meet you ' + query)
print('nice to meet you ' + query)
    


    
   
    
    


   
