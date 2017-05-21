from collections import deque
from player import Player
from deck import Deck
import time


class Game:

    players = []
    deck = Deck()

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

        # shuffle the deck and split the cards into the piles
        self.deck.shuffle()
        self.init_players(self.deck)
        self.create_piles(self.deck, self.stock_pile, self.discard_pile)

    def run(self):
        while True:
            self.tick()
            time.sleep(0.5)

    def init_players(self, deck):
        # hand every player seven cards from the deck
        for player in self.players:
            for x in range(7):
                player.cards.append(deck.pop())

    def create_piles(self, deck, stock_pile, discard_pile):
        # split remaining cards in the deck among the piles
        for card in deck.cards:
            stock_pile.append(card)
        # add the top card from the stock pile to the discard pile
        discard_pile.append(stock_pile.pop())

    def tick(self):
        for player in self.players:
            # querie player for a card
            card = player.play_card(self.discard_pile[-1])
            if(card is not None):
                self.discard_pile.append(card)
                print('Player {} played "{}!"'.format(player.name, card))
