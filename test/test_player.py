import unittest
from src.deck import Deck
from src.hand import Hand
from src.dealer import Dealer
from src.player import Player

#~~~~~~~~~~~~ Unit testing ~~~~~~~~~~~~~~#
# 3 As
# Arrange
# Act
# Assert


class PlayerTestCase(unittest.TestCase):

    def setUp(self):  # this method will be run before each test
        self.deck = Deck()
        self.dealer = Dealer(self.deck)
        self.player = Player("Sadiq")
        self.dealer.shuffle

    def tearDown(self):  # this method will be run after each tests
        pass

    # Given I play a game of blackjack
    # When I am dealt my opening hand
    # Then I have two cards
    def test_opening_hand(self):
        test_player = self.player
        test_dealer = self.dealer

        test_player.receive_card(test_dealer.deal_card())
        test_player.receive_card(test_dealer.deal_card())

        expected = test_player.hand.size

        self.assertEqual(expected, 2)

    # Given I have a valid hand of cards
    # When I choose to ‘hit’
    # Then I receive another card
    # And my score is updated
    def test_hit_on_valid_hand(self):

        # Arrange Valid hand
        test_player = self.player
        test_dealer = self.dealer
        test_dealer.shuffle

        test_player.receive_card(("10", 10))
        test_player.receive_card(("5", 5))
        hand_size_pre_hit = test_player.hand.size
        score_pre_hit = test_player.evaluate_hand()

        # Act
        # Does hit need to somehow receive a card in the function
        if(test_player.hit()):
            test_player.receive_card(test_dealer.deal_card())
            hand_size_post_hit = test_player.hand.size
            print(hand_size_post_hit)
            score_post_hit = test_player.evaluate_hand()
            print(score_post_hit)

        # Assert
        self.assertEqual(hand_size_post_hit, hand_size_pre_hit + 1)
        self.assertNotEqual(score_pre_hit, score_post_hit)

    # Test bust hand invalid
    def test_hand_bust(self):
        test_player = self.player

        test_player.receive_card(("10", 10))
        test_player.receive_card(("10", 10))
        test_player.receive_card(("10", 10))

        test_player.evaluate_hand()

        self.assertFalse(test_player.is_hand_valid())

    # Test hand 21 or under is valid
    def test_hand_valid(self):

        test_player = self.player
        test_player.receive_card(("10", 10))
        test_player.receive_card(("5", 5))
        test_player.receive_card(("A", 11))

        test_player.evaluate_hand()

        self.assertTrue(test_player.is_hand_valid())

    def test_king_ace(self):

        test_player = self.player
        test_player.receive_card(("K", 10))
        test_player.receive_card(("A", 11))

        score = test_player.evaluate_hand()

        self.assertEqual(score, 21)

    def test_king_queen_ace(self):

        test_player = self.player
        test_player.receive_card(("Q", 10))
        test_player.receive_card(("K", 10))
        test_player.receive_card(("A", 11))

        score = test_player.evaluate_hand()

        self.assertEqual(score, 21)

    def test_double_ace_nine(self):

        test_player = self.player
        test_player.receive_card(("9", 9))
        test_player.receive_card(("A", 11))
        test_player.receive_card(("A", 11))

        score = test_player.evaluate_hand()

        self.assertEqual(score, 21)

    # Test deal card only deals one card
    def test_deal_card(self):

        deal = self.dealer.deal_card()
        self.player.receive_card(deal)

        self.assertEqual(self.player.hand.size, 1)


if __name__ == '__main__':
    unittest.main()
