import wordle
import unittest

class Test_generate_word(unittest.TestCase):
    def test_return_type(self):
        self.assertEqual(len(wordle.generate_word()), 5)

    def test_length(self):
        self.assertIsInstance(wordle.generate_word(), str)

    def test_length(self):
        self.assertEqual(type(wordle.generate_word()), str)

class TestWord(unittest.TestCase):
    def test_init(self):
        new_word = wordle.Word("hello")
        self.assertFalse(new_word.correct)

if __name__ == '__main__':
    unittest.main()

    