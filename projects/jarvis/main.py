import speech_recognition as sr
import webbrowser
import pyttsx3
import requests
from openai import OpenAI
import os
from datetime import datetime

recognizer = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate', 175)

NEWS_API_KEY = os.getenv("NEWSAPI_KEY")


def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

def get_news():
    try:
        url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}"
        response = requests.get(url)
        if response.status_code != 200:
            speak("Failed to fetch news.")
            return
        articles = response.json().get("articles", [])
        if not articles:
            speak("No news available.")
            return
        speak("Here are the top headlines")
        for article in articles[:5]:
            speak(article["title"])
    except:
        speak("News service not working.")

def processCommand(c):
    c = c.lower()

    if "open google" in c:
        webbrowser.open("https://google.com")

    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")

    elif "open facebook" in c:
        webbrowser.open("https://facebook.com")

    elif "open linkedin" in c:
        webbrowser.open("https://linkedin.com")

    elif "time" in c:
        speak(datetime.now().strftime("%I:%M %p"))

    elif "news" in c:
        get_news()

    elif "exit" in c or "stop" in c:
        speak("Shutting down")
        exit()

 

def listen_command():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.2)
        audio = recognizer.listen(source, timeout=10, phrase_time_limit=5)
    return recognizer.recognize_google(audio)

if __name__ == "__main__":
    speak("Initializing Jarvis")
    while True:
        try:
            word = listen_command()
            if word.lower() == "jarvis":
                speak("Yes?")
                command = listen_command()
                processCommand(command)
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            speak("Speech service error")
        except:
            pass