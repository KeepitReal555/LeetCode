class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return len(nums)

        temp = nums[0]

        for num in nums[1:]:

            if num == temp:
                print(num)
                nums.remove(num)
            else:
                temp = num

        nums_len = len(nums)
        return nums_len

    def removeDuplicates2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, j = 0, 1
        if len(nums) <= 1:
            return len(nums)
        while True:
            if j == len(nums):
                break
            if nums[i] == nums[j]:
                j += 1
            else:
                nums[i + 1] = nums[j]
                i += 1
                j += 1
        print(i+1)
        return i + 1

nums = [1,1,2]
sol = Solution()
sol.removeDuplicates2(nums)