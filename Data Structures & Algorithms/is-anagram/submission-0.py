class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tList = list(t)
        for c in s:
            if c not in tList:
                return False
            tList.remove(c)

        if tList != []:
            return False

        return True