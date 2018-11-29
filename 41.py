class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for i in range(n):
#             print(i)
            while nums[i]>0 and nums[i]<=n and nums[i] != nums[nums[i]-1]:
                # print(nums)
                temp = nums[i]
                nums[i] = nums[nums[i]-1]
                nums[temp-1] = temp
#                 nums[i], nums[nums[i]-1] = nums[nums[i]-1], nums[i]
        # print(nums)
        for i in range(n):
            if nums[i] != i+1:
                return i+1
        return n+1
        