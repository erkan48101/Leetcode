class Solution(object):
    def maximumTripletValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_value = float('-inf')
        
        n = len(nums)
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    temp = (nums[i] - nums[j]) * nums[k]
                    if temp > max_value:
                        max_value = temp
        
        return max(0, max_value)