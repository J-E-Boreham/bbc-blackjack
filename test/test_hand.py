import unittest
from src.deck import Deck
from src.hand import Hand
#~~~~~~~~~~~~ Unit testing ~~~~~~~~~~~~~~#
# 3 As
# Arrange
# Act
# Assert


class HandTestCase(unittest.TestCase):

    def setUp(self):  # this method will be run before each test
        self.deck = Deck()
        #self.hand = Hand()

    def tearDown(self):  # this method will be run after each tests
        pass

    # any method beginning with 'test' will be run by unittest
    def test_opening_handsize(self):
        self.hand = Hand(self.deck.deal_opening_hand())
        number_of_cards = self.hand.hand_size
        self.assertEqual(number_of_cards, 2)


if __name__ == '__main__':
    unittest.main()
