class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = dict()
        for elem in nums:
            if elem in counts:
                counts[elem] += 1
            
            else:
                counts[elem] = 1

        sortedKeys = sorted(counts, key = counts.get, reverse = True)
        return sortedKeys[:k]
        