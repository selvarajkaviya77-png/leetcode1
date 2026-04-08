class Solution:
    def search(self, nums: List[int], target: int) -> int:
        past = nums[0]
        piv = 0
        temp_nums = []
        ans = -1
        found_pivot = False

        for i in range(len(nums)):
            if nums[i] < past:
                piv = i-1
                found_pivot = True
                break

        if not found_pivot:
            return self.search_helper(nums, 0, len(nums)-1, target)

        if target > nums[-1]:
            temp_nums = nums[:piv+1]
            ans = self.search_helper(temp_nums, 0, len(temp_nums) - 1, target)
            return ans
        else:
            temp_nums = nums[piv+1:]
            ans = self.search_helper(temp_nums, 0, len(temp_nums) - 1, target)
            if ans > -1:
                return ans + piv + 1
        return -1
    
    def search_helper(self, n, left, right, t):
        if left > right:
            return -1
        
        mid = (left + right)//2


        if n[mid] == t:
            return mid
        elif n[mid] < t:
            return self.search_helper(n, mid+1, right, t)
        else:
            return self.search_helper(n, left, mid-1, t)
        