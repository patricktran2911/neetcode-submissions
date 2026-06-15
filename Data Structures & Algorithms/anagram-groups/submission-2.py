class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        container = defaultdict(list)
        for word in strs:
            asciiSum = [0] * 26
            for c in word:
                asciiSum[ord(c) - ord('a')] += 1
            container[tuple(asciiSum)].append(word)
        return list(container.values())
            