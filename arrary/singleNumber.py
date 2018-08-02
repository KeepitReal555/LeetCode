class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if len(nums)<2:
            return nums[0]
        if nums[0] != nums[1]:
            print(nums[0])
            return nums[0]
        if nums[-1] != nums[-2]:
            print(nums[-1])
            return nums[-1]
        for i in range(1, len(nums) - 1):
            if nums[i] != nums[i - 1] and nums[i] != nums[i + 1]:
                print(nums[i])
                return nums[i]
    def singleNumber1(self, nums):
        '''
        直接用 按位异或运算符 ^
        当运算的两数相同时，结果为0，
        不同时，结果为差值的绝对数
        这样对整个数组做按位异或运算，其结果就是单独的数
        :param nums:
        :return:
        '''
        res = 0
        for num in nums:
            res = res ^ num
        print(res)
        return res



a = [2,2,13,13,3]
sol = Solution()
sol.singleNumber1(a)