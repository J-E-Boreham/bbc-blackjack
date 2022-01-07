from .player import Player

##### Class represeting a BlackJack Dealer ######

"""
	Inherits from Player as dealer is a type of player

    Attributes of a dealer
    - has a hand of cards - super
    - has a deck

    Required functionality
    (Super)
    - Receive a card
    - Request cards
    - Stand
    - Evaluate hand
    - Reveal hand

    Dealer specific
    -shuffle deck
    -deal card

"""


class Dealer(Player):

    def __init__(self, deck):
        super().__init__("Dealer")
        self.deck = deck

    def shuffle(self):
        self.deck.shuffle()

    def deal_card(self):
        return self.deck.deal_card()

    def deal_opening_hand(self):

        return self.deck.deal_opening_hand()
