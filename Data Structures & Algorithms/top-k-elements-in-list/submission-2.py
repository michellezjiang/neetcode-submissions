class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # counts = dict()
        # for elem in nums:
        #     if elem in counts:
        #         counts[elem] += 1
            
        #     else:
        #         counts[elem] = 1

        # sortedKeys = sorted(counts, key = counts.get, reverse = True)
        # return sortedKeys[:k]

        counts = dict()
        for elem in nums:
            counts[elem] = 1 + counts.get(elem, 0)

        bucket = [[] for i in range(len(nums) + 1)]

        for key, val in counts.items():
            bucket[val].append(key)

        result = []

        for i in range(len(bucket) - 1, 0, -1):
            result.extend(bucket[i])
            if len(result) == k:
                return result
        