from src.hand import Hand


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
    # def update_hand(self):
    #     self.hand.update()

    def receive_card(self, card):
        self.hand.add_card(card)

    def hit(self):
        if self.is_hand_valid():
            return True
        else:
            return False

    def stand(self):
        if self.is_hand_valid():
            # Evaluate final score and return final score
            self.hand.score = self.evaluate_hand()
            return self.hand.score

    def is_hand_valid(self):
        if self.evaluate_hand() <= 21:
            return True
        else:
            return False

    def evaluate_hand(self):
        return self.hand.get_score()

    def show_hand(self):
        self.hand.reveal()
