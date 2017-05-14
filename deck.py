from card import Card
from card import Suits


class Deck:
    """This class represents an entire deck. A deck is
    the complete collection of cards that are going to be used in the game"""

    """        spade    heart    diamond    club    """
    __suits = ['\u2660', "\u2665", "\u2666", "\u2663"]

    """the actual deck"""
    cards = []

    def __init__(self):
        self.cards = self.createDeck()

    def __str__(self):
        return "\nCards : {}".format(self.cards)

    def __repr__(self):
        return "\n<Deck(cards={}>".format(self.cards)

    def createDeck(self):
        """use a simple list comprehension to combine the suits enum and an
        integer range and create the entire 52 card deck"""
        return [Card(suit, rank) for suit in Suits for rank in
                range(1, 14)]

    def shuffle():
        """"""
