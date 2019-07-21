def break_words(stuff):
    """This function breaks up words for us"""
    words = stuff.split(" ")
    return words


def sort_words(words):
    """sorts the words"""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after poping """
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """Prints the last word """
    word = words.pop()
    print(word)
    
def sort_sentence(sentence):
    """Take full sentence and arrange that in alphabetic"""
    words = break_words(sentence)
    return sort_words(words)
    
def print_first_and_last(sentence):
    """Print first and last word of the sentence"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)
    
def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last words"""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
    
    
    
# line = "hello i am a web developer at jaaga"
# words = break_words(line)
# print(sort_words(words))
# print(words)
# print(sort_sentence(line))
# print_first_and_last_sorted(line)