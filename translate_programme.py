from googletrans import Translator, constants
from pprint import pprint
import pyttsx3
import speech_recognition as sr
import pyaudio


try:
  while True:
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    def speak(audio):
        engine.say(audio)
        engine.runAndWait()

    def takeCommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            speak("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...")
            speak("Recognizing...")
            query = r.recognize_google(audio, language='en-in')

        except Exception as e:
            print(e)
            print("Sir, kindly say that again.")
            speak("Sir, kindly say that again.")
            return "none"
        return query

    print("What you wanna to translate: ")
    speak("What you wanna to translate: ")
    user_input = takeCommand().lower()
    print("In which Language?")
    speak("In which Language?")
    user_input2 = takeCommand().lower()

    translator = Translator()

    translation = translator.translate(user_input, dest=user_input2)

    print(f"'{user_input}'({translation.src}) in {user_input2} is ---> {translation.  text}({translation.dest}) ")

    speak(f"'{user_input}' in {user_input2} is  {translation.  text} ")

    print('Do you want to translate more? Yes/No')
    speak('Do you want to translate more? Yes/No')
    yes_no = takeCommand().lower()

    if yes_no == "yes":
      continue
    elif yes_no =="no":
      print("Bye sir, Hope you enjoyed my programme.")
      print('{0:*^100}'.format("THIS PROGRAM IS PROGRAMMED BY RAYHAN MAHMUD"))
      speak("Bye sir, Hope you enjoyed my programme. This Prgramme is Programmed by Rayhan Mahmud")
      exit()


except Exception as e:
  while True:
    print(e)
    user_input = input("What you wanna to translate: ")
    user_input2 = input("In which Languase: ")

    translator = Translator()

    translation = translator.translate(user_input, dest=user_input2)
    print(f"'{user_input}'({translation.src}) in {user_input2} is ---> {translation.  text}({translation.dest}) ")

    yes_no = input("Do you wanna translate more? yes/no:")

    if yes_no == "yes":
      continue
    elif yes_no =="no":
      print("Bye sir, Hope you enjoyed my programme.")
      print('{0:*^100}'.format("THIS PROGRAM IS PROGRAMMED BY RAYHAN MAHMUD"))
      exit()
