import tkinter as tk
from tkinter import ttk
from threading import Thread
import speech_recognition as sr  # recognise speech
from gtts import gTTS
import random
import webbrowser  # open browser
import os
import playsound
from time import ctime
import time

from main import voice_data, speak


def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True


r = sr.Recognizer()


def record_audio():

    with sr.Microphone() as source:
        r.energy_threshold = 500
        r.adjust_for_ambient_noise(source, 1.2)
        r.pause_threshold = 1
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.RequestError:
            voice_data = 'Sorry, the service is down'
        except sr.UnknownValueError:
            voice_data = 'Recognizing...'
        return voice_data.lower()


def respond(voice_data):
    # 1: greeting
    if there_exists(["hey", "hi", "hello", "wake up", "hai"]):
        greetings = ["hey", "hey, what's up? ", " how can I help you", "I'm listening", "hello"]
        greet = greetings[random.randint(0, len(greetings) - 1)]
        speak(greet)

    # 2: name
    if there_exists(["your name", "what i call you", "what is your good name"]):
        name = record_audio("my name is Vavo stand for virtual assistance version One. what's your name?")
        speak('Nice to meet you ' + name)
        speak('how can i help you ' + name)

    # 3: Origin

    if there_exists(["who are you", "your inventor", "invented you", "created you", "who is your developer"]):
        greetings = ["I am Virtual Voice Assistant",
                     "I am developed by mr.abhijeet as a voice assistance"]  # You can Add your name
        greet = greetings[random.randint(0, len(greetings) - 1)]
        speak(greet)

    if there_exists(["what is your age", "how old are you", "when is your birthday"]):
        greetings = ["I came into this world in march 2021"]
        greet = greetings[random.randint(0, len(greetings) - 1)]
        speak(greet)

    # 3: Take care's
    if there_exists(
            ["how's everything", "how ia everything", "how are you", "how are you doing", "what's up", "whatsup"]):
        greetings = ["I am well ...thanks for asking ", "i am well", "Doing Great"]
        greet = greetings[random.randint(0, len(greetings) - 1)]
        speak(greet)

    # 3: greeting
    if there_exists(["What are you doing", "what you doing", "doing"]):
        greetings = ["nothing", "nothing...,just working for you", "Nothing much"]
        greet = greetings[random.randint(0, len(greetings) - 1)]
        speak(greet)

        # 4.1: time
    if there_exists(
            ["what's  the time", "tell me the time", "what time is it", "what is the time", "time is going on"]):
        time = ctime().split(" ")[3].split(":")[0:2]
        if time[0] == "00":
            hours = '12'
        else:
            hours = time[0]
        minutes = time[1]
        time = f'{hours} {minutes}'
        speak(time)

        # 5: search wekiapedia
    if there_exists(["wikipedia"]):
        search = record_audio('What do you want to search for?')
        url = 'https://en.wikipedia.org/wiki/' + search
        webbrowser.get().open(url)
        speak('Here is what I found for' + search)

    # 5: search
    if there_exists(["do google", "search google", "on google", "search for", "in google"]):
        search = record_audio('What do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        speak('Here is what I found for' + search)

    # 5.6: opening youtube
    if there_exists(["open the youtube", "open youtube"]):
        url = 'https://www.youtube.com/'
        webbrowser.get().open(url)
        speak('Opening')

    # 5.7: opening google
    if there_exists(["open the  google", "open google"]):
        url = 'https://www.google.com/'
        webbrowser.get().open(url)
        speak('Opening')
        # 5.7: opening gemail
    if there_exists(["open gmail", "open email", "open my email", "check email"]):
        url = 'https://mail.google.com/'
        webbrowser.get().open(url)
        speak('Opening')

    # 5.5: find location
    if there_exists(["location"]):
        location = record_audio('What is the locatio n?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        speak('Opening map of' + location)

    # 6: search youtube
    if there_exists(["search youtube", "search the youtube", "search in youtube", "in youtube", "on youtube"]):
        search = record_audio('What do you want to search for?')
        r.pause_threshold = 2
        url = 'https://www.youtube.com/results?search_query=' + search
        webbrowser.get().open(url)
        speak('Here is what I found')

        # OS shutdown
    if there_exists(["shutdown system", "system off", "shutdown the system", "system shutdown"]):
        speak('Okay system will off in 30 seconds')
        os.system("shutdown /s /t 30")

    if there_exists(["good", "thank you", "thanks", "well done"]):
        greetings = ["my pleasure", "Don't mention", "Thanks for your compliment", "No problem.",
                     "Thank you, it makes my day to hear that."]
        greet = greetings[random.randint(0, len(greetings) - 1)]
        speak(greet)

    if there_exists(["exit", "quit", "sleep", "shut up", "close"]):
        greetings = ["Going offline ! you can call me Anytime", "Okay ,you can call me Anytime", "See you later",
                     "See you soon", "Have a good day."]
        greet = greetings[random.randint(0, len(greetings) - 1)]
        speak(greet)
        exit()


def on_submit():
    user_input = entry.get().lower()
    if user_input:
        t = Thread(target=respond, args=(user_input,))
        t.start()


def on_voice_assistant_click():
    t = Thread(target=lambda: respond(record_audio()))
    t.start()


app = tk.Tk()
app.title('Voice Assistant')

frame = ttk.Frame(app, padding='10')
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

entry = ttk.Entry(frame, width=50)
entry.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

submit_button = ttk.Button(frame, text='Submit', command=on_submit)
submit_button.grid(row=0, column=2, padx=5, pady=5)

voice_assistant_button = ttk.Button(frame, text='Voice Assistant', command=on_voice_assistant_click)
voice_assistant_button.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

app.mainloop()
