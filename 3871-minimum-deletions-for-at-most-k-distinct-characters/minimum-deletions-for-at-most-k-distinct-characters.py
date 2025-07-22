class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        freq = {}
        for i in s:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        if len(freq) <= k:
            return 0  

       
        freqs = sorted(freq.values())

        deletions = 0
        to_remove = len(freq) - k
        for i in range(to_remove):
            deletions += freqs[i]

        return deletions
