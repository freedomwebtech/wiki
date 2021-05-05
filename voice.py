import speech_recognition as sr
from gtts import gTTS
import wikipedia
import os
def audio():
    r=sr.Recognizer()
    with sr.Microphone() as source:
         print("say somthing")
         audio=r.listen(source)
         data=r.recognize_google(audio)
         print(data)
         return data

def speak(a):
    tts = gTTS(text=a, lang='en')
    tts.save("audio.mp3")
    os.system("mpg321 audio.mp3")



def wiki():
    a=audio()
    result = wikipedia.summary(a, sentences = 2) 
    speak (result)



wiki()
