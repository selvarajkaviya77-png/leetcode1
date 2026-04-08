class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float("-inf")
        current_sum = 0
        for num in nums:
            current_sum += num
            if current_sum > res:
                res = current_sum
            if current_sum < 0:
                current_sum = 0

        return res

        