def pigLatin(string):
    
    # format text, remove non-alpha, lowercase

    string = [i for i in string.lower()]
    for i,letter in enumerate(string):
        if not letter.isalpha() and letter != ' ':
            del(string[i])
    string = ''.join(string)

    # translate words

    string = [i for i in string.split()]
    for i,word in enumerate(string):
    
        # if starts with vowel, add "ay" to the end
        
        if word[0] in 'aeiou':
            # rearrange word
            word = word + 'ay'
            
        # if starts with consonant(s), move them to the end, add ay
        
        else:
        	# figure out what is the first vowel
            vowels = []
            for _,letter in enumerate(word):
                if letter in 'aeiou':
                    vowels.append(letter)
            # rearrange word
            word = word.partition(vowels[0])
            word = ''.join(word[1:]) + word[0] + 'ay'

        string[i] = word

    string = ' '.join(string)
    print(string)

pigLatin('Lorem Ipsum is simply dummy text of the printing and typesetting industry. Yes!')