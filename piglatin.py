# import regex
import re

# the translator
def translate(text):
	
	# format text
	text = [i for i in text.lower()]
	for i,letter in enumerate(text):
		# remove if not alpha, space
		if not letter.isalpha() and not letter in ' ':
			del(text[i])
	text = ''.join(text)

	# split and translate
	text = [i for i in text.split()]
	for i,word in enumerate(text):
	
		# if starts with a consonant, move first letter(s) to end
		if not word[0] in 'aeiou':

			# figure out what is the first vowel
			vowels = []
			for _,letter in enumerate(word):
				if letter in 'aeiou':
					vowels.append(letter)
			
			# rearrange word
			if len(vowels) > 0:				
				word = word.partition(vowels[0])
				word = ''.join(word[1:]) + word[0]
		
		# add "ay" to the end
		text[i] = word + 'ay'
		
	# put it all back together
	text = ' '.join(text)

	# print the translated text
	return(text)

# prompt for a phrase
def prompt():

	# add some space at the start
	print("\n" * 100)
	
	# ask for a phrase to translate
	while True:

		text = input('\nEnter some text to translate into Pig Latin > ')

		# is there at least one letter in the phrase?
		if not re.search('[a-zA-Z]+',text):
			print("Sorry, that's not valid text. Try again!")
		# are there any digits?
		elif re.search('[0-9]+',text):
			print("Sorry, no digits allowed. The translator can't handle them. Try again!")
		else:
			break

	# translate it
	print("Got it! Here's your translated text:\n")
	print(translate(text))
	
	# add some spacing
	print("\n" * 3)

#prompt()