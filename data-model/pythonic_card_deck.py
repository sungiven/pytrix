import collections

Card = collections.namedtuple("Card", ["rank", "suit"])
# `collections.namedtuple` is used to construct a simple class to represent individual cards.
# We can use `namedtuple` to build classes of objects that are just bundles of attributes
# with no custom methods, like a database record.


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        """
        A deck responds to the `len()` function by returning thhe number of cards in it.\n
        Examples:
            >>> deck = FrenchDeck()
            >>> len(deck)
            52
        """
        return len(self._cards)

    def __getitem__(self, position):
        """
        Reading specific cards from the deck is easy with __getitem__.\n
        Examples:
            >>> deck[0]
            Card(rank='2', suit='spades')
            >>> deck[-1]
            Card(rank='A', suit='hearts')
            >>> from random import choice
            >>> choice(deck)
            Card(rank='Q', suit='diamonds')
            >>> deck[:3]
            [Card(rank='2', suit='spades'), Card(rank='3', suit='spades'), Card(rank='4', suit='spades')]
            >>> deck[12::13] # pick just the aces
            [Card(rank='A', suit='spades'), Card(rank='A', suit='diamonds'), Card(rank='A', suit='clubs'), Card(rank='A', suit='hearts')]
        """
        return self._cards[position]
