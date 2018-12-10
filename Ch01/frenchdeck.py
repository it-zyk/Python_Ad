# 一摞Python风格的纸牌
import collections
from random import choice
# collections.namedtuple 构建了一个简单的类来表示一张纸牌
Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


# deck = FrenchDeck()
# print("len(deck) : " + str(len(deck)))
# print(choice(deck))
#
# print(deck[12::13])  # 先抽出索引是 12 的那张牌，然后每隔 13 张牌拿 1 张
#
#
# def spades_high(card):
#     rank_value = FrenchDeck.ranks.index(card.rank)
#     return rank_value * len(suit_values) + suit_values[card.suit]
