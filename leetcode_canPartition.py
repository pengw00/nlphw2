class Solution:
    def caPartition(self, nums):
        S = sum(nums)
        if S%2 == 1: return false
        nums = sorted(nums, reverse= True)

        def DFS(start, curSum):
            if curSum == S//2: return True
            if curSum + sum(nums[start:]) < S//2: return False
            if curSum >= S//2: return False

