class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "empty set"
        result = ""
        for word in strs:
            result += word
            result += '\n'
        result = result[:-1]
        return result

    def decode(self, s: str) -> List[str]:
        if s == "empty set":
            return []
        result = s.split('\n')
        return result
