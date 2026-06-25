class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1

        result = list(freq.values())
        result.sort(reverse = True)

        result = result[:k]

        finalResult = []

        for key in freq:
            if freq[key] in result:
                finalResult.append(key)


        return finalResult
        