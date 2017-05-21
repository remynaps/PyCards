

class Player:

    name = "default"
    cant_play = False
    # order dos not matter for the player so normal list will do
    cards = []

    def __init__(self, name):
        self.name = name

    def __str__(self):
        """"""

    def play_card(self, top_card, stock_pile):
        try:
            # find a card that can be placed on the top_card
            play_card = next(card for card in self.cards if (card.suit ==
                             top_card.suit) | (card.rank == top_card.rank))
            # take that card
            self.cards.remove(play_card)
            return play_card
        except Exception:
            return self.take_card(stock_pile)

    def take_card(self, stock_pile):
        # skip turn if no cards left on stock pile
        if(len(stock_pile) < 1):
            print('{} skipping turn. Stock pile too small'.format(self.name))
            """flow control to avoid a situation where game keeps going if
            no one can play"""
            self.cant_play = True
            return
        # take a card from the stock pile
        new_card = stock_pile.pop()
        self.cant_play = False
        # add the card to our own cards
        self.cards.append(new_card)
        print('{} doesnt have a suitable card. took card: {}'
              .format(self.name, new_card))
        return
