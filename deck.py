from card import Card


class Deck:
    """This class represents an entire deck. A deck is
    the complete collection of cards that are going to be used in the game"""

    """        spade    heart    diamond    club    """
    __suits = ['\u2660', "\u2665", "\u2666", "\u2663"]
    __ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q",
               "K", "A"]

    cards = []

    def __init__(self):
        self.cards = createDeck()

    def createDeck():
        """use a simple list comprehension to combine the two lists and
        create an entire deck"""
        return [(suit + rank) for suit in __suits for rank in __ranks]

    def shuffle():


    def __str__(self):
        print cards
