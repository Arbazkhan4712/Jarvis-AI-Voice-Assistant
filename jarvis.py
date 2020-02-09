import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    speak("Welcome back!")
    Time= datetime.datetime.now().strftime("%I:%M:%S")
    print(Time)
    speak(f"The current time is {Time}")



def wiki():
    query = "Iphone"
    results = wikipedia.summary(query, sentences=2)
    speak("according to wikipedia")
    print(results)
    speak(results)



def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"AK47 Said:{query}\n")

    except Exception as e:
        print(e)
        print("Say that again Please...")
        speak("Say that again Please...")
        return "None"
    return query

takeCommand()