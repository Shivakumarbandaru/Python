from playsound import playsound
number = input("Enter a number: ")
try:
	for digit in number:
		playsound(digit + ".mp3")
except Exception as e:
	print("Error occured.", e)

