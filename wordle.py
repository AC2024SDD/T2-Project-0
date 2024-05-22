import random

words_array = [
    "apple", "beach", "cloud", "dance", "eagle", "flame", "green", "happy", "igloo", "jelly",
    "knife", "lemon", "magic", "night", "ocean", "pizza", "queen", "radio", "snake", "toast",
    "umbra", "vault", "waltz", "xenon", "yacht", "zebra", "abide", "baker", "charm", "dream",
    "earth", "flour", "grape", "heart", "ivory", "joker", "kiosk", "laser", "mango", "novel",
    "opera", "piano", "quick", "ruler", "salsa", "table", "unity", "virus", "witty", "xerox",
    "yield", "amber", "broom", "champ", "daisy", "emote", "fairy", "giant", "happy",
    "ideal", "jumbo", "kitty", "lunar", "mirth", "noble", "olive", "party", "quest", "rider",
    "sable", "tango", "ultra", "vibes", "wager", "xylon", "young", "zesty", "agile", "bloom",
    "chord", "dodge", "elite", "fable", "grain", "heist", "irate", "joust", "karma", "loyal",
    "mirth", "novel", "oasis", "pluto", "quack", "raven", "siren", "trick", "ultra", "venom",
    "wacky", "xerox", "yield", "zebra", "acorn", "brave", "cabin", "daisy", "elope", "fancy",
    "glide", "hazel", "ivory", "jewel", "knots", "lemon", "marsh", "nurse", "opera", "pupil",
    "quilt", "rifle", "sweat", "train", "utens", "vigor", "widen", "yacht", "zebra", "abide",
    "baker", "charm", "dream", "earth", "flour", "grape", "heart", "ivory", "joker", "kiosk",
    "laser", "mango", "novel", "opera", "piano", "quick", "ruler", "salsa", "table", "unity",
    "virus", "witty", "xerox", "yield", "amber", "broom", "champ", "daisy", "emote",
    "fairy", "giant", "happy", "ideal", "jumbo", "kitty", "lunar", "mirth", "noble", "olive",
    "party", "quest", "rider", "sable", "tango", "ultra", "vibes", "wager", "xylon", "young",
    "zesty", "agile", "bloom", "chord", "dodge", "elite", "fable", "grain", "heist", "irate",
    "joust", "karma", "loyal", "mirth", "novel", "oasis", "pluto", "quack", "raven", "siren",
    "trick", "ultra", "venom", "wacky", "xerox", "yield", "zebra", "acorn", "brave", "cabin",
    "daisy", "elope", "fancy", "glide", "hazel", "ivory", "jewel", "knots", "lemon", "marsh",
    "nurse", "opera", "pupil", "quilt", "rifle", "sweat", "train", "utens", "vigor", "widen",
    "yacht", "zebra", "abide", "baker", "charm", "dream", "earth", "flour", "grape", "heart",
    "ivory", "joker", "kiosk", "laser", "mango", "novel", "opera", "piano", "quick", "ruler",
    "salsa", "table", "unity", "virus", "witty", "xerox", "yield", "amber", "broom",
    "champ", "daisy", "emote", "fairy", "giant", "happy", "ideal", "jumbo", "kitty", "lunar",
    "mirth", "noble", "olive", "party", "quest", "rider", "sable", "tango", "ultra", "vibes",
    "wager", "xylon", "young", "zesty", "agile", "bloom", "chord", "dodge", "elite", "fable",
    "grain", "heist", "irate", "joust", "karma", "loyal", "mirth", "novel", "oasis", "pluto",
    "quack", "raven", "siren", "trick", "ultra", "venom", "wacky", "xerox", "yield", "zebra",
    "acorn", "brave", "cabin", "daisy", "elope", "fancy", "glide", "hazel", "ivory", "jewel",
    "knots", "lemon", "marsh", "nurse", "opera", "pupil", "quilt", "rifle", "sweat", "train",
    "utens", "vigor", "widen", "yacht", "zebra", "abide", "baker", "charm", "dream", "earth",
    "flour", "grape", "heart", "ivory", "joker", "kiosk", "laser", "mango", "novel", "opera",
    "piano", "quick", "ruler", "salsa", "table", "unity", "virus", "witty", "xerox", "yield",
    "amber", "broom", "champ", "daisy", "emote", "fairy", "giant", "happy", "ideal",
    "jumbo", "kitty", "lunar", "mirth", "noble", "olive", "party", "quest", "rider", "sable",
    "tango", "ultra", "vibes", "wager", "xylon", "young", "zesty"
]

def generate_word():
    random_number = random.randint(0, len(words_array) - 1)
    word = words_array[random_number]
    
    '''Returns a five letter word as String
    Parameters:
    None
    
    Returns:
    str: Random 5 letter word
    '''
    # Pulls a word from massive array
    return word

def test_generate_word():
    assert type(generate_word() ) == str, "Method returned datatype other that str"
    assert isinstance(generate_word(), str), "Method returned datatype other that str"
    assert len(generate_word()) == 5, "Word returned was not 5 letters"

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

    def test(self):
        print('Test Passed')

    def guess(self, word):
        new_guess = Word(word, self.key_word)
        new_guess.set_states(self.key_word)
        self.guesses.append(new_guess)
        if new_guess.correct:
            self.game_over = True
        return None

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

if __name__ == '__main__':
    test()
    #play()
