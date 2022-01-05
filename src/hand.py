

class Hand:

    def __init__(self, cards):
        self.cards = cards
        self.score = 0
        self.hand_size = len(self.cards)

    def add_card(self, card):
        self.cards.append(card)

    def get_score(self):
        local_score = 0
        aces = 0
        for c in self.cards:
            if c[0] == "A":
                aces += 1
            local_score += c[1]

        self.score = self.handle_aces(aces, local_score)
        return self.score

    @staticmethod
    def handle_aces(aces, local_score):
        local_score -= (aces * 11)
        # handle aces as 1s and 11s
        if aces == 1:
            if local_score <= 10:
                local_score += 11
                return local_score

            elif local_score <= 20:
                local_score += 1
                return local_score

        elif aces == 2:
            if local_score <= 9:
                local_score += 12
                return local_score

            elif local_score <= 19:
                local_score += 2
                return local_score

        elif aces == 3:
            if local_score <= 8:
                local_score += 13
                return local_score

            elif local_score <= 18:
                local_score += 3
                return local_score

        elif aces == 4:
            if local_score <= 7:
                local_score += 14
                return local_score

            elif local_score <= 17:
                local_score += 4
                return local_score
        else:
            return local_score

    def reveal(self):
        for c in self.cards:
            print(c[0], end=" ")
