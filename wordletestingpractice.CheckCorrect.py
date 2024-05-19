from wordle import * #imports word function from word
import unittest

def test_check_correct(self):
		assert type(Word.check_correct(self)) == bool, "Returned value of incorrect type"  #provide assertion and if wrong returns error, use string for documentation of what error is occurring.
		
		assert len(Word.check_correct(self)) == 5, "length should be 5"
		assert not Word.check_correct(self) == Word.check_correct(self), "test should return Boolean"

		assert isinstance(Word.check_correct(self),bool) 
		"method returned datatype other than boolean" #message after is what is produced
	
testword = 'strive'
#testword = 'party'
test_check_correct('strive')