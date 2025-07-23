class Solution(object):
    def findMaxConsecutiveOnes(self, a):
        max_count = 0
        count = 0
        i = 0
        while i < len(a):
            if a[i] == 1:
                count += 1
                if count > max_count:
                    max_count = count
            else:
                count = 0
            i += 1
        return max_count