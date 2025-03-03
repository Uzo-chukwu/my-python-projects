import unittest
from hangman import hangman


class MyTestCase(unittest.TestCase):
    def test_plus_one(self):
        actual = hangman.plus_one([9,9,9])
        expected = [1,0,0,0]
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
