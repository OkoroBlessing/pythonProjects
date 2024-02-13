import speech_recognition as sr
from time import ctime
import webbrowser
import time
import playsound
import os #to remove th file generated 
import random #to randomly generare file name 
#from gtts import gTTS
import pyttsx3


r = sr.Recognizer()#responsible for actually recognizing speech. 
# it initializes the 

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            alexis_speak (ask)
        audio = r.listen(source) #listen for the audio via source
        voice_data =''
        try:
            voice_data = r.recognize_google(audio) #converts audio to text
        #puts what you say into a variable     
        except sr.UnknownValueError:
            alexis_speak("sorry, I didn't recognize that")
        except sr.RequestError:
            alexis_speak("Sorry my speech service is down")
        return voice_data
    
# def alexis_speak(audio_string):
#     tts = gTTS(text=audio_string,lang='en')
#     r = random.randint(1,1000000)
#     audio_file = 'audio-' +str(r) + '.mp3'
#     tts.save(audio_file)
#     playsound.playsound(audio_file)
#     alexis_speak(audio_string)
#     os.remove(audio_file)

def alexis_speak(audio_string):
    engine = pyttsx3.init()
    engine.say(audio_string)
    engine.runAndWait()
    
    
    
# REPLACE ALL THE PRINTS WITH THE ALEXIS SPEAK
def respond(voice_data):
    if "what is your name" in voice_data:
        alexis_speak("my name is alexis")
    if "what time is it " in voice_data:
        alexis_speak(ctime())
    if "search" in voice_data:
        search = record_audio('what do you want to search for')
        url = 'https://google.com/search?q=' +search
        webbrowser.get().open(url)
        alexis_speak("Here is what I found for "+search)
    if "find location" in voice_data:
        location = record_audio('what is the location')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        alexis_speak("Here is the location of "+ location)
        
    if "exit" in voice_data:
        exit()
        
time.sleep(3)    
alexis_speak("how can i help you ")
while (1):
    voice_data = record_audio()
    respond(voice_data)
