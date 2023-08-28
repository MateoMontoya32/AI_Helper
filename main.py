import speech_recognition as sr
from gtts import gTTS
import wikipedia
import webbrowser
import time
import os
import random
import re
import requests


# Initialize speech recognition
recognizer = sr.Recognizer()

# Initialize text-to-speech engine


def speak(text):
    tts = gTTS(text)
    tts.save("output.mp3")
    os.system("mpg321 output.mp3")  # Use a suitable audio player command for your system


def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        print("Recognizing speech...")
        query = recognizer.recognize_google(audio).lower()
        print(f"You said: {query}")
        return query
    except sr.UnknownValueError:
        return "unknown"
    except sr.RequestError:
        return "error"


def process_command(command):
    if "hello" in command:
        speak("Hello! How can I assist you?")
    elif "how are you" in command:
        speak("I'm just a computer program, but I'm functioning well. Thanks for asking!")
    elif "wikipedia" in command:
        query = re.sub(r"wikipedia", "", command).strip()
        result = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia:")
        speak(result)
    elif "open website" in command:
        url = re.search(r"open website (.+)", command).group(1)
        webbrowser.open(url)
    elif "time" in command:
        current_time = time.strftime("%I:%M %p")
        speak(f"The current time is {current_time}.")
    elif "search" in command:
        query = re.search(r"search (.+)", command).group(1)
        search_url = f"https://www.google.com/search?q={query}"
        webbrowser.open(search_url)
    elif "exit" in command:
        speak("Goodbye!")
        exit()


if __name__ == "__main__":
    speak("Hello! I'm your voice assistant. How can I assist you?")

    while True:
        command = listen()

        if command == "unknown":
            speak("Sorry, I didn't catch that.")
        elif command == "error":
            speak("There was an error in processing your request.")
        else:
            process_command(command)
