from src.hand import Hand
from src.moves import Moves

##### Class represeting a BlackJack Player ######


"""
    Attributes of a player
    - has a hand of cards

    Required functionality
    - Receive a card
    - Request cards
    - Stand
    - Evaluate hand
    - Reveal hand

"""


class Player(object):

    def __init__(self, name):
        self.hand = Hand()
        self.name = name
        self.is_playing = True

    def receive_card(self, card):
        self.hand.add_card(card)

    def hit(self, dealer):
        self.receive_card(dealer.deal_card())

    def stand(self):
        self.is_playing = False

    def bust(self):
        self.is_playing = False

    def is_hand_valid(self):
        if self.evaluate_hand() <= 21:
            return True
        else:
            return False

    def evaluate_hand(self):
        return self.hand.update_score()

    def show_hand(self):
        self.hand.reveal()

    def take_turn(self):
        # stick or hit
        player_input = input("\nhit or stand?\n")
        player_input.strip()

        # try catch invalid input error
        if player_input.lower() == "hit":
            return Moves.HIT
        if player_input.lower() == "stand":
            return Moves.STAND
        else:
            print("Invalid move selected, please try again")
            self.take_turn()
