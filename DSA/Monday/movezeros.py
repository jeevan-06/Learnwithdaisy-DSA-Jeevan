class Solution:
    def moveZeros(self,nums):
        position=0
        for i in range (len(nums)):
            if nums[i] !=0:
                nums[i],nums[position]=nums[position],nums[i]
                position= position+1