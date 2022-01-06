from src.deck import Deck
from src.hand import Hand
from src.dealer import Dealer
from src.player import Player


def check_scores(dealer_score, player_score):


def play():

    # Initialise game - Create a deck a dealer and a player
    game_deck = Deck()
    dealer = Dealer(game_deck)
    player1 = Player()
    dealer.shuffle()

    # Deal opening hand
    player1.receive_card(dealer.deal_card())
    dealer.receive_card(dealer.deal_card())
    player1.receive_card(dealer.deal_card())
    dealer.receive_card(dealer.deal_card())

    game_over = False

    while not game_over:

        print("Dealer score: = %s" % dealer.evaluate_hand())
        print("Player score: = %s" % player1.evaluate_hand())

        # If not bust offer player another card
        if player1.is_hand_valid():

            # stick or hit
            soh = input("\nhit or stand?\n")

            # try catch invalid input error
            if soh == "hit":
                if player1.hit():
                    card = dealer.deal_card()
                    print("card just dealt, ", card)

                    player1.receive_card(card)
                    print("Updated Score is %s" % player1.evaluate_hand())

            elif soh == "stand":

                player1.stand()
                print("Player's final score is %s" % player1.score)
                player1.show_hand()

        else:
            game_over = True
            player1.show_hand()
            print("BUST! Your Score is %s" % player1.evaluate_hand())

    # if player1.finalscore > dealer.finalscore:
    #     print("Player1 wins!")
    # elif player1.finalscore == dealer.finalscore:
    #     print("It's a draw play again")
    # else:
    #     print("The house wins again...")


if __name__ == '__main__':
    play()
