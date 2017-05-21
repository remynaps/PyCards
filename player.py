

class Player:

    name = "default"

    # order dos not matter for the player so normal list will do
    cards = []

    def __init__(self, name):
        self.name = name

    def __str__(self):
        """"""

    def play_card(self, top_card, stock_pile):
        try:
            play_card = next(card for card in self.cards if (card.suit ==
                             top_card.suit) | (card.rank == top_card.rank))
            self.cards.remove(play_card)
            return play_card
        except Exception:
            new_card = self.take_card(stock_pile)
            self.cards.append(new_card)
            print('{} cant play. took card: {}'.format(self.name, new_card))
            return None

    def take_card(self, stock_pile):
        return stock_pile.pop()
