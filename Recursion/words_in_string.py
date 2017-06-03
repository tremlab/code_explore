"""from udemy course

Create a function called word_split() which takes in a string phrase 
and a set list_of_words. The function will then determine which words 
from the list can be found in the string, and retruns the found words in a list.
"""

def word_split(phrase,list_of_words):
    
    if len(phrase) == 0:
        return None
    
    word_matches = []
    
    for word in list_of_words:
        if phrase.startswith(word):
            word_matches.append(word)
    
            more_matches = word_split(phrase[len(word):], list_of_words)
            if more_matches:
                word_matches.extend(more_matches)
    
    return word_matches

print word_split('themanran',['the','ran','man'])
print word_split('ilovedogsJohn',['i','am','a','dogs','lover','love','John'])


# the exmaple of 'lover' 'love' is a problem... once one was found, 
 #   it is sliced out of the string and could not be used to match the other word.
    