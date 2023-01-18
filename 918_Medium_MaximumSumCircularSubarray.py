class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        array_sum = 0
        curr_max = -math.inf
        max_so_far = -math.inf
        curr_min = math.inf
        min_so_far = math.inf

        for i in range(len(nums)):
            
            array_sum += nums[i]
            curr_max = max(curr_max + nums[i], nums[i])
            max_so_far = max(max_so_far, curr_max)

            curr_min = min(curr_min + nums[i], nums[i])
            min_so_far = min(min_so_far, curr_min)

        if (min_so_far == array_sum):
            return max_so_far

        return max(max_so_far, array_sum - min_so_far)
 
