
#from hand import Hand


class Player:

    def __init__(self, opening_hand):

        self.hand = opening_hand

    # def update_hand(self):
    #     self.hand.update()

    def hit(self):
        if self.is_hand_valid():
            return True

    def stand(self):
        if self.is_hand_valid():
            return self.evaluate_hand()

    def is_hand_valid(self):
        print(type(self.evaluate_hand()))
        if self.evaluate_hand() <= 21:
            return True
        else:
            return False

    def evaluate_hand(self):
        return self.hand.get_score()

    def show_hand(self):
        self.hand.reveal()
