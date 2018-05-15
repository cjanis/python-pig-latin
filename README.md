# Python Pig Latin

Translate text into Pig Latin using Python

## How it works

This script converts English text in Pig Latin following these steps:

- Strips non-alpha or single space characters from input text
- Converts input text to all lower case
- For words that start with consonants, moves all consonants before the first vowel to the end of the word ("the" becomes "ethay" not "hetay")
- For words that start with vowels, nothing is changed, only the suffix is added
- Adds suffix "ay" to the end of words

## Instructions

Install with Pip/PyPi in the command line interface:

```
pip install pig-latin
```

In your Python code, import the library:

```
import piglatin
```

Call the translator in your code:

```
piglatin.translate('Your text goes here!')
```

Your text will be translated into Pig Latin and returned as a string.