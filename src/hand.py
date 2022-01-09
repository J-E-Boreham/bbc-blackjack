##### Class represeting a BlackJack Hand ######
"""
    Attributes of a Hand
    - a collection of cards
    - has a score
    - size - number of cards

    Required functionality
    - add a card 
    - return the it's score
    - reveal it's cards


"""


class Hand:

    def __init__(self):
        self.cards = []
        self.score = 0
        self.size = 0

    def add_card(self, card):
        self.cards.append(card)
        self.size = len(self.cards)
        self.score = self.update_score()

    def update_score(self):
        updated_score = 0
        aces = 0

        # Sum card values of hand
        for card in self.cards:
            if card[0] == "A":
                aces += 1
            updated_score += card[1]

        # Handle Aces as 1 if score above 21
        while updated_score > 21 and aces > 0:
            updated_score -= 10
            aces -= 1
        return updated_score

    # Display card face
    def reveal(self):
        for card in self.cards:
            print(card[0], end=" ")