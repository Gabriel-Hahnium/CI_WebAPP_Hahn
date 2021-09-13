import random

#this function is given a list of words and selects one at random
def random_word(list_of_words):
    number_of_words = len(list_of_words) #get the length of the words list
    random_word_number = random.randint(0,number_of_words - 1) #pick a random number up to the end of the list
    random_word = list_of_words[random_word_number] #select the word at the number spot
    return random_word #hand it back
