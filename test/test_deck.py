import unittest
from src.deck import Deck

#~~~~~~~~~~~~ Unit testing ~~~~~~~~~~~~~~#
# 3 As
# Arrange
# Act
# Assert


class DeckTestCase(unittest.TestCase):

    def setUp(self):  # this method will be run before each test
        self.deck = Deck()

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
        # preshuffle deck vs post shuffle
        first_card = self.deck.cards[0]
        self.assertEqual(("2", 2), first_card)
        self.deck.shuffle()
        self.assertNotEqual(first_card, self.deck.cards[0])

    # test deal opening hand deals 2 cards
    def test_deal_opening_hand(self):
        number_of_cards = len(self.deck.deal_opening_hand())
        self.assertEqual(number_of_cards, 2)

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
