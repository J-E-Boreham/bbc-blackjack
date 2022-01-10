from src.deck import Deck
from src.dealer import Dealer
from src.player import Player
from src.moves import Moves


def initialise_game():
    # Initialise game - Create a deck a dealer and players
    game_deck = Deck()
    dealer = Dealer(game_deck)
    dealer.shuffle()

    num_players = int(input("How many players wish to play the dealer?\n"))
    players = []

    # create quantity of players
    for x in range(num_players):
        players.append(Player("Player " + str(x + 1)))

    # Add dealer to end of list so they are always last to play
    players.append(dealer)

    # Deal each player 2 cards
    for _ in range(2):
        for p in players:
            p.receive_card(dealer.deal_card())

    return players


def compare_scores(players):
    dealer = players.pop()
    print("~~~~~~~~~~~~Final Scores~~~~~~~~~~~~\n")
    print("Dealer's final score : %s" % dealer.hand.score + "\n")
    for player in players:
        print(player.name + "'s final score is: %s" % player.hand.score + "\n")

        if dealer.hand.score < player.hand.score < 22:
            print(player.name + " wins! Collect your prize")
        elif player.hand.score == dealer.hand.score < 22:
            print("It's a draw split the pot and play again")
        elif player.hand.score < dealer.hand.score < 22:
            print("The house wins again...")
        elif player.hand.score < 22 < dealer.hand.score:
            print("Dealer is bust " + player.name + " wins! Collect your prize")
        elif dealer.hand.score < 22 < player.hand.score:
            print("Dealer is bust " + player.name + " The house wins again...")
        else:
            print("You're all bust. No winners here")


def all_players_bust(players):
    non_dealer_players = players[:-1]
    all([True if player.hand.score > 21 else False for player in non_dealer_players])


def play():
    players = initialise_game()
    dealer = players[-1]

    # Each player plays blackjack in turn ending with the dealer
    for active_player in players:

        dealer.show_initial_hand()
        print(active_player.name + "'s score: = %s" %
              active_player.hand.score)

        # If not bust player takes a turn
        while active_player.is_playing:

            # Dealer has to stick on 17 or above hit
            if active_player.name == "Dealer":
                if active_player.hand.score > 16 or all_players_bust(players):
                    player_move = Moves.STAND
                else:
                    player_move = Moves.HIT
            else:
                player_move = active_player.take_turn()

            # Player turn
            if player_move == Moves.HIT:
                active_player.hit(dealer)

                print(active_player.name + "'s score is now %s" %
                      active_player.hand.score)
                active_player.show_hand()
                # if hand is no longer valid, player has bust. break and move to next player
                if not active_player.is_hand_valid():
                    print("player has bust!")
                    active_player.bust()

            elif player_move == Moves.STAND:
                active_player.stand()
                print("\n" + active_player.name + "'s final score is %s " %
                      active_player.hand.score)
                active_player.show_hand()
                print("")

        # Dealer is the last to play always - now we can calculate final scores
        if active_player.name == "Dealer":
            compare_scores(players)


if __name__ == '__main__':
    play()
