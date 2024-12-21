from collections import OrderedDict

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dictionary = OrderedDict()
        pattern = list(pattern)
        split_str = s.split()

        if len(pattern) != len(split_str):
            return False

        for p, ss in zip(pattern, split_str):
            if p in dictionary:
                if ss != dictionary[p]:
                    return False
            else:
                if ss in dictionary.values():
                    return False       
                dictionary[p] = ss
        return True