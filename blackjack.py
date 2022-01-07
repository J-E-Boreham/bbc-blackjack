from src.deck import Deck
from src.hand import Hand
from src.dealer import Dealer
from src.player import Player


def compare_scores(dealer, player1):
    if player1.hand.score > dealer.hand.score:
        print("\n" + player1.name + " wins!")
    elif player1.hand.score == dealer.hand.score:
        print("\nIt's a draw split the pot and play again")
    else:
        print("\nThe house wins again...")


def play():

    # Initialise game - Create a deck a dealer and a player
    game_deck = Deck()
    dealer = Dealer(game_deck)
    player1 = Player("Bob")
    dealer.shuffle()

    # Deal opening hand
    player1.receive_card(dealer.deal_card())
    dealer.receive_card(dealer.deal_card())
    player1.receive_card(dealer.deal_card())
    dealer.receive_card(dealer.deal_card())

    game_over = False

    players = [player1, dealer]
    active_player = 0

    while not game_over:

        passive_player = (active_player + 1) % 2
        print("\n" + players[active_player].name + "'s score: = %s" %
              players[active_player].evaluate_hand())
        # print("Player score: = %s" % player1.evaluate_hand())

        # If not bust offer player another card
        if players[active_player].is_hand_valid():

            # stick or hit
            soh = input("\nhit or stand?\n")

            # try catch invalid input error
            if (soh == "hit"):
                if players[active_player].hit():
                    card = dealer.deal_card()
                    print("card just dealt, ", card, "\n")

                    players[active_player].receive_card(card)
                    print(players[active_player].name + " updated Score is %s" %
                          players[active_player].evaluate_hand())

            elif soh == "stand":

                players[active_player].stand()
                print(players[active_player].name + "'s final score is %s \n" %
                      players[active_player].evaluate_hand())
                players[active_player].show_hand()

                # Game always finishes on the dealer
                if players[active_player].name == "Dealer":
                    compare_scores(dealer, player1)
                    game_over = True

                active_player = passive_player

        else:
            game_over = True
            players[active_player].show_hand()
            print("\nBUST! " + players[active_player].name + " Your Score is %s" %
                  players[active_player].evaluate_hand())
            print(players[passive_player].name + " is the winner!")


if __name__ == '__main__':
    play()
