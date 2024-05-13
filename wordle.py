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
        self.state = None #Can be set to 'Correct', 'Misplaced' or 'Wrong'

class Word():
    def __init__(self, word, key_word = None):
        self.letters = []
        for letter in word:
            current_letter = Letter(letter)
            self.letters.append(current_letter)
        if key_word:
            self.set_states(key_word)
        self.correct = self.check_correct()

    
    def set_states(self, key_word):
        count = 0
        for letter in self.letters:
            if letter.letter == key_word[count]:
                letter.state = 'Correct'
            elif letter.letter in key_word:
                letter.state = 'Misplaced'
            else: letter.state = 'Wrong'
            count += 1
    
    def check_correct(self):
        for letter in self.letters:
            if not letter.state == 'Correct':
                return False
        return True
        
class Game():
    def __init__(self):
        self.key_word = generate_word()
        self.guesses = []
        self.game_over = False

    def guess(self, word):
        new_guess = Word(word, self.key_word)
        new_guess.set_states(self.key_word)
        self.guesses.append(new_guess)
        if new_guess.correct:
            self.game_over = True

def play():
    game = Game()
    while not game.game_over:
        try:
            guess = input('Guess:').lower()
            game.guess(guess)
            for i in game.guesses:
                grid = []
                for letter in i.letters:
                    if letter.state == 'Correct':
                        grid.append(letter.letter)
                    elif letter.state == 'Misplaced':
                        grid.append('('+letter.letter+')')
                    else:
                        grid.append('#')
                print(grid)
                if i.correct:
                    print('Congratulations! You win!')
        except:
            pass

play()
