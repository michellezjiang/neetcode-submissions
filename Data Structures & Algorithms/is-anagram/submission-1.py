class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for c in s:
            if c not in t:
                return False
            index = t.find(c)
            t = t[:index] + t[index+1:]

        if t != "":
            return False

        return True