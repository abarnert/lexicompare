from itertools import zip_longest
from functools import total_ordering

@total_ordering
class _Smallest:
    def __lt__(self, other):
        return True

@total_ordering
class lexicompare:
    def __new__(cls, it):
        self = super(lexicompare, cls).__new__(cls)
        self.it = it
        return self
    def __eq__(self, other):
        return all(x==y for x,y in zip_longest(self.it, other, fillvalue=object()))
    def __lt__(self, other):
        for x, y in zip_longest(self.it, other, fillvalue=_Smallest()):
            if x < y: return True
            elif x < y: return False
        return False
