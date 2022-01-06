import unittest
from src.deck import Deck
from src.hand import Hand
from src.player import Player

#~~~~~~~~~~~~ Unit testing ~~~~~~~~~~~~~~#
# 3 As
# Arrange
# Act
# Assert


class PlayerTestCase(unittest.TestCase):

    def setUp(self):  # this method will be run before each test
        self.deck = Deck()
        #self.hand = Hand()

    def tearDown(self):  # this method will be run after each tests
        pass

    def test_hit_on_valid_hand(self):
        self.hand = Hand(self.deck.deal_opening_hand())
        number_of_cards = self.hand.hand_size
        self.assertEqual(number_of_cards, 2)


if __name__ == '__main__':
    unittest.main()
