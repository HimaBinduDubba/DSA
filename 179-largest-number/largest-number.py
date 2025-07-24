class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        
        # Sort based on repeating each string (to mimic custom comparator)
        nums.sort(key=lambda x: x*10, reverse=True)

        # Join the sorted strings
        res = ''.join(nums)

        # Handle case where result is like "0000"
        return '0' if res[0] == '0' else res