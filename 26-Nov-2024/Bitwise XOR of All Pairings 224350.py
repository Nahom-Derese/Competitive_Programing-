# Problem: Bitwise XOR of All Pairings - https://leetcode.com/problems/bitwise-xor-of-all-pairings/description/?envType=problem-list-v2&envId=brainteaser

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        
        if len(nums1)&1:
            if len(nums2)&1:
                return reduce(lambda x, y: x ^ y, nums1+nums2)
            else:
                return reduce(lambda x, y: x ^ y, nums2)
        else:
            if len(nums2)&1:
                return reduce(lambda x, y: x ^ y, nums1)
            else:
                return 0

