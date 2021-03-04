import pyttsx3
playAudio = pyttsx3.init()
playAudio.say(input("Enter a text: "))
playAudio.runAndWait()
