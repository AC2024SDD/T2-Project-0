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





  

def wordle():
    pass

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
        
