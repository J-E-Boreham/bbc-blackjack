from src.deck import Deck
from src.hand import Hand
from src.player import Player


def play():
        # Create deck and shuffle it
    game_deck = Deck()
    game_deck.shuffle()

    # Deal a player an opening hand
    #player1_hand = Hand(game_deck.deal_opening_hand())
    player1_hand = Hand([("A", 11), ("A", 11)])
    player1 = Player(player1_hand)

    # Evaluate hand check if valid and display score to player via terminal
    print("Hand Score is %s" % player1.evaluate_hand())

    player1.show_hand()

    # Offer player chance to hit or stick
    while player1.is_hand_valid():
        if input("\nhit or stick?\n") == "hit":
            if player1.hit():
                player1_hand.add_card(game_deck.deal_card())
                print("Hand Score is %s" % player1.evaluate_hand())
                player1.show_hand()
        else:
            final_score = player1.stand()
            print("Player's final score is %s" % final_score)
            player1.show_hand()

    print("BUST! Your Score is %s" % player1.evaluate_hand())


if __name__ == '__main__':
    play()
