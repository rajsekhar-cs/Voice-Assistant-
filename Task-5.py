#!/usr/bin/env python
# coding: utf-8

# In[3]:


import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import datetime
import random
import os

# ---------------------------
# Initialize Voice Engine
# ---------------------------
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 170)


def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()


# ---------------------------
# Greeting Function
# ---------------------------
def greet_user():
    hour = datetime.datetime.now().hour

    if hour < 12:
        speak("Good Morning!")

    elif hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am your personal voice assistant.")
    speak("How can I help you today?")


# ---------------------------
# Listen Function
# ---------------------------
def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("\nListening...")

        recognizer.adjust_for_ambient_noise(source, duration=1)

        try:
            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=8
            )

            command = recognizer.recognize_google(audio)

            print("You:", command)

            return command.lower()

        except sr.WaitTimeoutError:
            return ""

        except sr.UnknownValueError:
            speak("Sorry, I didn't understand that.")
            return ""

        except Exception as e:
            print("Error:", e)
            speak("An error occurred.")
            return ""


# ---------------------------
# Time
# ---------------------------
def tell_time():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {current_time}")


# ---------------------------
# Date
# ---------------------------
def tell_date():
    today = datetime.datetime.now().strftime("%d %B %Y")
    speak(f"Today's date is {today}")


# ---------------------------
# Wikipedia Search
# ---------------------------
def wikipedia_search(command):
    try:
        query = command.replace("wikipedia", "")
        query = query.replace("search", "")

        speak("Searching Wikipedia")

        result = wikipedia.summary(query, sentences=2)

        speak(result)

    except Exception:
        speak("Sorry, I couldn't find anything.")


# ---------------------------
# Joke Generator
# ---------------------------
def tell_joke():

    jokes = [
        "Why do programmers hate nature? It has too many bugs.",
        "Why was the computer cold? It left its windows open.",
        "I would tell you a UDP joke, but you might not get it.",
        "Why did the programmer quit his job? Because he didn't get arrays."
    ]

    speak(random.choice(jokes))


# ---------------------------
# Note Taking
# ---------------------------
def save_note():

    speak("What should I write?")

    note = listen()

    if note:

        with open("notes.txt", "a") as file:
            file.write(note + "\n")

        speak("Note saved successfully.")


# ---------------------------
# Open Websites
# ---------------------------
def open_website(command):

    websites = {
        "google": "https://www.google.com",
        "youtube": "https://www.youtube.com",
        "github": "https://github.com",
        "gmail": "https://mail.google.com",
        "wikipedia": "https://www.wikipedia.org"
    }

    for name, url in websites.items():

        if name in command:
            speak(f"Opening {name}")
            webbrowser.open(url)
            return

    speak("Website not found.")


# ---------------------------
# Open Applications
# Ubuntu Version
# ---------------------------
def open_application(command):

    apps = {
        "calculator": "gnome-calculator",
        "files": "nautilus",
        "terminal": "gnome-terminal"
    }

    for app, cmd in apps.items():

        if app in command:
            speak(f"Opening {app}")
            os.system(cmd)
            return

    speak("Application not available.")


# ---------------------------
# Command Processor
# ---------------------------
def process_command(command):

    if "hello" in command or "hi" in command:
        speak("Hello Raj!")

    elif "time" in command:
        tell_time()

    elif "date" in command:
        tell_date()

    elif "joke" in command:
        tell_joke()

    elif "note" in command:
        save_note()

    elif "wikipedia" in command:
        wikipedia_search(command)

    elif "open" in command:

        if any(site in command for site in
               ["google", "youtube", "github", "gmail", "wikipedia"]):

            open_website(command)

        else:
            open_application(command)

    elif "thank you" in command:
        speak("You're welcome.")

    elif "who are you" in command:
        speak("I am your personal voice assistant created using Python.")

    elif "exit" in command or "stop" in command or "goodbye" in command:
        speak("Goodbye. Have a nice day.")
        return False

    else:
        speak("Sorry, I don't know that command yet.")

    return True


# ---------------------------
# Main Program
# ---------------------------
def main():

    greet_user()

    running = True

    while running:

        command = listen()

        if command:
            running = process_command(command)


if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:




