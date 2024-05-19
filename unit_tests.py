
import wordle

def test_generate_word():
    assert type(wordle.generate_word()) == str, "Returned word of incorrect type"
    assert len(wordle.generate_word()) == 5, "Length should be 5"
    assert not wordle.generate_word() == wordle.generate_word(), "Should return different words each time"
    
test_generate_word()