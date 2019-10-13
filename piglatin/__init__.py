# import regex
import re

# the translator
def translate(text):
		
	# format text
	text = [i for i in text.lower()]
	for i,letter in enumerate(text):
		# remove if not alpha, space
		if not letter.isalpha() and not letter in ' ':
			text[i] = ''
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