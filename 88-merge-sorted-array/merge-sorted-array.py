class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums3=nums1[:m]+nums2[:n]
        nums1[:]=sorted(nums3)