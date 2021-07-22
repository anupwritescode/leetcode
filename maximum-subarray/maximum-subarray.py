class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        left = 0
        right = 0
        max_sum = -100000
        
        local_max = 0
        
        for num in nums :
            local_max += num
            if local_max > max_sum :
                max_sum = local_max
            if local_max < 0 :
                local_max = 0
        return max_sum
        
