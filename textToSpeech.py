"""from gtts import gTTS
from playsound import playsound
mytext = input("Enter text: ")
file = "text.mp3"
language = 'en'
myobject = gTTS(text = mytext, lang = language, slow = False)
myobject.save(file)
playsound(file)"""
import pyttsx3
playAudio = pyttsx3.init()
playAudio.say(input("Enter a text: "))
playAudio.runAndWait()