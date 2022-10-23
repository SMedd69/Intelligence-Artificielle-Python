import speech_recognition as sr
import pyttsx3 as ttx

listener=sr.Recognizer()
engine=ttx.init()
voice=engine.getProperty('voices')
engine.setProperty('voice', 'french')

def parler(text):
    engine.say(text)
    engine.runAndWait()

def ecouter():

    try:
        with sr.Microphone() as source:
            print("Parlez maintenant")
            voix=listener.listen(source)
            command=listener.recognize_google(voix, language='fr-FR')
                
    except:
        pass
    return command

def lancer_assistant():
    command=ecouter()
    print(command)
    if 'Bonjour' in command:
        text='bonjour, ca vas ?'
        parler(text)
    
lancer_assistant()