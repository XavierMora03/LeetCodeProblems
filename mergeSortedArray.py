from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        j = 0
        i = 0
        for _ in range(max(m,n)):
            if nums1[i] > nums2[j]:
                nums1.insert(i,nums2[j])
                j+=1
            i+=1
