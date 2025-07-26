class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        set1=set(nums1)
        set2=set(nums2)
        l1= list(set1.intersection(set2))
        if not l1:
            return -1
        l1.sort()
        return l1[0]
        