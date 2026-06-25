class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        index = dict()

        for word in strs:
            key = str(sorted(word))
            if key in index:
                index[key].append(word)

            else:
                index[key] = [word]

        return list(index.values())

        
        