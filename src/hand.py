

##### Class represeting a BlackJack Hand ######
"""
    Attributes of a Hand
    - a collection of cards
    - has a score
    - handsize

    Required functionality
    - add a card 
    - return the it's score
    - reveal it's cards


"""


class Hand:

    def __init__(self):
        self.cards = []
        self.score = 0
        self.hand_size = len(self.cards)

    def add_card(self, card):
        self.cards.append(card)
        self.hand_size = len(self.cards)

    def get_score(self):
        local_score = 0
        aces = 0

        # Sum card values of hand
        for c in self.cards:
            if c[0] == "A":
                aces += 1
            local_score += c[1]

        # Handle Aces if Bust
        while(local_score > 21 and aces > 0):
            local_score -= 10
            aces -= 1
        self.score = local_score
        return self.score

    def reveal(self):
        for c in self.cards:
            print(c[0], end=" ")
