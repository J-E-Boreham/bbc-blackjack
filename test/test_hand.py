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
        self.hand = Hand()

    def tearDown(self):  # this method will be run after each tests
        pass

    # any method beginning with 'test' will be run by unittest
    def test_number_of_cards(self):
        number_of_cards = len(self.deck.cards)
        self.assertEqual(number_of_cards, 52)

    def test_deck_not_empty(self):
        number_of_cards = len(self.deck.cards)
        self.assertIsNotNone(number_of_cards)

    # test shuffle works
    def test_deck_shuffle(self):
        first_card = self.deck.cards[0]
        self.assertEqual(("2", 2), first_card)
        self.deck.shuffle()
        self.assertNotEqual(first_card, self.deck.cards[0])

    # test deal initial hand deals 2 cards
    def test_deal_opening_hand(self):
        number_of_cards = len(self.deck.deal_opening_hand())
        self.assertIsNotNone(number_of_cards)
        self.assertEqual(number_of_cards, 2)

    # check each card only has 4 instances
    def test_four_twos(self):
        self.assertEqual(self.deck.cards.count(("2", 2)), 4)

if __name__ == '__main__':
    unittest.main()
