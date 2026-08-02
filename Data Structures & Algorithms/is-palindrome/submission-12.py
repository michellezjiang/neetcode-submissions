class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        index1 = 0
        index2 = len(s)-1

        while index1 < index2:

            while index1 < index2 and not s[index1].isalnum():
                index1 += 1

            while index2 > index1 and not s[index2].isalnum():
                index2 -= 1

            if s[index1] != s[index2]:
                return False

            index1 += 1
            index2 -= 1

        return True


        