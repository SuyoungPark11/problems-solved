from collections import Counter

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counter = Counter(list(s))      
        values = list(counter.values())
        return all([False if sum(values) / len(values) != v else True for v in values])
