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