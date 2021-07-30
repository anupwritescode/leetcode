class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        l = {}
        majority = len(nums) // 2
        for num in nums :
            if num in l:
                l[num] += 1
            else :
                l[num] = 1
            
            if l[num] > majority :
                return num
        
