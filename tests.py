import unittest
from game import Game
from card import Card
from collections import deque


class Test_card_game(unittest.TestCase):

    def test_empty_stock_pile(self):
        game = Game()
        game.stock_pile = deque()
        # create impossible card
        game.discard_pile = deque([Card("test", 20)])
        game.run()
        self.assertEqual(4, (len(game.cant_play_players)), 'cant play')

if __name__ == '__main__':
    unittest.main()
