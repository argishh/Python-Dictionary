import pyttsx3
import json
from difflib import get_close_matches

def dictionary():
	data = json.load(open("data.json"))

	engine = pyttsx3.init('sapi5')

	voices = engine.getProperty('voices')
	rate = engine.getProperty('rate')

	engine.setProperty('voice', voices[1].id)
	engine.setProperty('rate', rate-10)
	
	def speak(text):
		engine.say(text)
		engine.runAndWait()
		return 

	def translate(w):
		w = w.lower()

		if w in data:
			return data[w]
		
		elif w.title() in data:
			return data[w.title()]
		
		elif w.upper() in data: # For uppercase words like USA or NATO
			return data[w.upper()]
		
		elif len(get_close_matches(w, data.keys())) > 1:
			closeMatch = get_close_matches(w, data.keys(), n=5)[0]
			choice = input(f"Did you Mean '{closeMatch}'?. Enter 'Y' if YES or 'N' if NO: ")
			
			if choice == "Y" or choice == "y":
				return translate(closeMatch) 

			elif choice == "N" or choice == "n":
				print("Sorry, The Word doesn't Exist!")
				return None
			
			else:
				print("Choice Not Identified!")
				return None
		
		else:
			print("Sorry, The Word doesn't Exist, Please Double Check it!")
			return None

	word = input("\nEnter Word: ")
	result = translate(word)[:7]
	[print("->", i,end="\n") for i in result]
	speak(result[0])

while True:
	dictionary()