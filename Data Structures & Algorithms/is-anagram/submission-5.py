class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sortedS = sorted(s)
        # sortedT = sorted(t)
        # return sortedS == sortedT
        
        if len(s) != len(t): return False

        sCounts = dict()
        for letter in s:
            if letter in sCounts:
                sCounts[letter] += 1
            else:
                sCounts[letter] = 1

        tCounts = dict()
        for letter in t:
            if letter in tCounts:
                tCounts[letter] += 1
            else:
                tCounts[letter] = 1

        for letter in sCounts:
            if letter not in tCounts or sCounts[letter] != tCounts[letter]:
                return False

        return True
        