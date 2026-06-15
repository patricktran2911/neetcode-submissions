class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        container = defaultdict(int)
        for num in nums:
            container[num] += 1
        result = [0] * (k)
        for e in range(0,k):
            maxCount = 0
            for key in container.keys():
                if container[key] > maxCount:
                    maxCount = container[key]
                    result[e - 1] = key
            container[result[e-1]] = 0
        return result

