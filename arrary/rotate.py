class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        temp = nums[:]
        if k <= 0 or length<=1:
            return
        else:
            for index in range(length):
                if index+k <= length-1:
                    nums[index+k] = temp[index]
                else :
                    new_index = (index+k) - (length)
                    if new_index < length-1:
                        nums[new_index] = temp[index]
                    else:
                        new_index = new_index % length
                        nums[new_index] = temp[index]

        print(nums)