def wordle():
    pass

def generate_word():
    '''Returns a five letter word as String
    Parameters:
    None
    
    Returns:
    str: Random 5 letter word
    '''
    # Pulls a word from Adam's csv file
    return "stump" #For testing purposes

class Letter():
    def __init__(self, letter):
        self.letter = letter
        self.state = 'undefined'

class Word():
    def __init__(self,word):
        self.letters = []
        for letter in word:
            current_letter = Letter(letter)
            self.letters.append(current_letter)
        
