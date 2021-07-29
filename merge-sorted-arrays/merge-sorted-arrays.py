class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        num1_index = 0
        num2_index = 0
        while num2_index < n :
            if num1_index >= (m + num2_index) :
                nums1.insert(num1_index, nums2[num2_index])
                num2_index += 1
                nums1.pop()
            elif nums1[num1_index] > nums2[num2_index] :
                nums1.insert(num1_index, nums2[num2_index])
                num2_index += 1
                nums1.pop()
            
            num1_index += 1
