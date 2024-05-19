from wordle import * #imports word function from word
import unittest

def test_check_correct(value):
		assert type(word.check_correct()) == bool, "Returned value of incorrect type"  #provide assertion and if wrong returns error, use string for documentation of what error is occurring.
		
		assert len(word.check_correct()) == 5, "length should be 5"
		assert not word.check_correct() == word.check_correct(), "test should return Boolean"

		assert isinstance(word.check_correct(),bool) 
		"method returned datatype other than boolean" #message after is what is produced
	
word = 'strive'
#worde = 'party'
test_check_correct('strive')