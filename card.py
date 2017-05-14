from enum import Enum


class Suits(Enum):
    spades = 1,
    hearts = 2,
    diamonds = 3,
    clubs = 4


class Card:

    """rank is int internally and is translated to char when requested"""
    rank = 0

    """default to hearts (this is overridden by the constructor)"""
    suit = Suits.hearts

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        """we build the two dictionaries here, because the only use for the
        string representation of the letters and suits is displaying the card
        to the user. The rest of the application only cares about the int and
        the enum representation"""

        """build a dictionary to handle 'special' cards in the deck.
        these are cards whose rank is not a number"""
        specials = {1: 'A', 11: 'J', 12: 'Q', 13: 'K'}

        """build a dictionary to handle the suits."""
        suits = {Suits.spades: '\u2660',
                 Suits.hearts: '\u2665',
                 Suits.diamonds: '\u2666',
                 Suits.clubs: '\u2663'}

        """retrieve the string representation of the suit and the rank"""
        letter = specials.get(self.rank, str(self.rank))
        suit = suits.get(self.suit, str(self.suit))

        return "%s%s" % (suit, letter)
