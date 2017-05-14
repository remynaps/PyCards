class Card:

    """rank is int internally and is translated to char when requested"""
    rank = 0
    suit = ''

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        """build a dictionary to handle 'special' cards in the deck.
        by handling these cards here, the internal type of the rank can
        still be an int"""
        letters = {1: 'A', 11: 'J', 12: 'Q', 13: 'K'}
        letter = letters.get(self.rank, str(self.rank))
        return "%s%s" % (self.suit, letter)
