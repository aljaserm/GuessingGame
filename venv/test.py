import unittest
import main

class RestGame(unittest.TestCase):
    def test_input(self):
        answer=5
        guess=5
        result= main.checkResult(guess,answer)
        self.assertTrue(result)

    def test_wrong_guess(self):
        answer = 0
        guess = 5
        result = main.checkResult(guess, answer)
        self.assertFalse(result)

    def test_Wrong_Number_input(self):
        answer = 11
        guess = 5
        result = main.checkResult(guess, answer)
        self.assertFalse(result)

    def test_input_wrong_type(self):
        result = main.run_guess(5, '11')
        self.assertFalse(result)

if __name__=='__main__':
    unittest.main()