from collections import deque
from player import Player
from deck import Deck


class Game:

    players = []
    deck = Deck()

    """flow control to avoid a situation where game keeps going when
    no one can play"""
    cant_play_players = []

    """create a stock pile and a descard pile. deque is used to get a LIFO
    data structure to represent stack of cards"""
    stock_pile = deque()
    discard_pile = deque()

    def __init__(self):
        # init players
        self.players.append(Player("Rick"))
        self.players.append(Player("Morty"))
        self.players.append(Player("Birdperson"))
        self.players.append(Player("Goldenfold"))

        # first we shuffle the deck
        self.deck.shuffle()
        # then we hand every player his/her cards
        self.deal_cards(self.deck)
        # and finally we split the remaining cards into the piles
        self.create_piles(self.deck, self.stock_pile, self.discard_pile)

    def deal_cards(self, deck):
        # hand every player seven cards from the deck
        for player in self.players:
            player_cards = []
            for x in range(7):
                # pop 7 cards from the deck and append them to new list
                player_cards.append(deck.pop())
            # actually hand the cards to the player
            player.cards = player_cards
            print('{} has been dealt: {}'.format(player.name, player.cards))

    def create_piles(self, deck, stock_pile, discard_pile):
        # split remaining cards in the deck among the piles
        for card in deck.cards:
            stock_pile.append(card)
        # add the top card from the stock pile to the discard pile
        discard_pile.append(stock_pile.pop())
        # index -1 is fastest way to peek top of deque
        print('Top card is: {}'.format(discard_pile[-1]))

    def tick(self):
        for player in self.players:
            # check if the player can still place cards
            if(player.cant_play and player not in self.cant_play_players):
                self.cant_play_players.append(player)

            # querie player for a card
            card = player.play_card(self.discard_pile[-1], self.stock_pile)
            if(card is not None):
                self.discard_pile.append(card)
                print('{} plays {}'.format(player.name, card))
            # check if we have one card left and report if we do
            if(len(player.cards) == 1):
                print('{} has one card remaining!'.format(player.name))
            # check if we have one card left and report if we do
            if(len(player.cards) == 0):
                print('{} has won!'.format(player.name))
                # end game
                return False
        # keep playing
        return True

    def run(self):
        playing = True
        while playing:
            playing = self.tick()
            if(len(self.cant_play_players) == len(self.players)):
                playing = False
                print('No one can play anymore. Ending game')
