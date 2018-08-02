class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 2:
            return False
        if len(nums) != len(set(nums)):
            return True
        return False

a = [3,3]
sol = Solution()
sol.containsDuplicate(a)