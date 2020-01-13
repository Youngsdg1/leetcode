class Solution(object):
    def hasGroupsSizeX(self, deck):
        from collections import Counter
        dct = collections.Counter(deck)
        N = len(deck)
        for X in xrange(2, N+1):
            if N % X == 0:
                if all(v % X == 0 for v in dct.values()):
                    return True
        return False
