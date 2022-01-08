import unittest
import copy
from src.deck import Deck
from src.dealer import Dealer

#~~~~~~~~~~~~ Unit testing ~~~~~~~~~~~~~~#
# 3 As
# Arrange
# Act
# Assert


class DeckTestCase(unittest.TestCase):

    def setUp(self):  # this method will be run before each test
        self.deck = Deck()
        self.dealer = Dealer(self.deck)

    def tearDown(self):  # this method will be run after each tests
        pass

    # any method beginning with 'test' will be run by unittest
    def test_number_of_cards(self):
        number_of_cards = len(self.deck.cards)
        self.assertEqual(number_of_cards, 52)

    # test shuffle works
    def test_deck_shuffle(self):
        # preshuffle deck vs post shuffle
        preshuffle_deck = [("2", 2), ("3", 3), ("4", 4),
                           ("5", 5), ("6", 6), ("7", 7),
                           ("8", 8), ("9", 9), ("10", 10),
                           ("J", 10), ("Q", 10), ("K", 10),
                           ("A", 11)] * 4
        deck_to_shuffle = self.deck

        self.assertEqual(preshuffle_deck, deck_to_shuffle.cards)
        deck_to_shuffle.shuffle()
        self.assertNotEqual(preshuffle_deck, deck_to_shuffle)

    # test dealing depleates deck
    def test_deck_depletion(self):

        self.dealer.deal_opening_hand()
        self.assertEqual(len(self.dealer.deck.cards), 50)

    # check each card only has 4 instances
    def test_four_of_each(self):

        cards = [("2", 2), ("3", 3), ("4", 4),
                 ("5", 5), ("6", 6), ("7", 7),
                 ("8", 8), ("9", 9), ("10", 10),
                 ("J", 10), ("Q", 10), ("K", 10),
                 ("A", 11)]

        for card in cards:
            self.assertEqual(self.deck.cards.count(card), 4)

if __name__ == '__main__':
    unittest.main()
