class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        while True:
            if val in nums:
                nums.remove(val)
            else:
                return(len(nums))