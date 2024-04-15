import speech_recognition as sr
import subprocess as sp
import os

def ouvir_microfone():

    audio_Input = sr.Recognizer()

    with sr.Microphone() as source:
        
        #Shreya = "ON"  
        
        Open = "Open"

        print("Hello my name is Shreya pleased to help you")

        audio_Input.adjust_for_ambient_noise(source)
        print("Say something: ")
        audio = audio_Input.listen(source)
        try:
            # valid
            frase = audio_Input.recognize_google(audio,language='en-IN')
            print("You said: " + frase)
        except: 
            # google could not validate
            print("Speech not recognised")
            return False

        if Open in frase:
            print('sucess') 
        return True
while True:
    if ouvir_microfone():
        # got a valid response
        break


