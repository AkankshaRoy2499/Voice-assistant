import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening.............')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            # print(command)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
            else:
                pass
    except:
        pass
    return command

def run_alexa():
     command = take_command()
     print(command)
     if 'play' in command:
         song= command.replace('play', '')
         talk('playing'+ song)
         pywhatkit.playonyt(song)
     elif 'time' in command:
         time= datetime.datetime.now().strftime('%I:%M:%p')
         print(time)
         talk('Current time is' + time)
     elif 'who is' in command:
         person= command.replace('who is', ' ')
         info = wikipedia.summary(person, 1)
         print(info)
         talk(info)
     elif 'do you love me alexa?' in command:
          print('I am madly in love with you Akanksha')
     elif 'joke' in command:
          talk(pyjokes.get_joke())
     else:
         talk('Can you please repeat yourself?')





run_alexa()
