class solution:
    def twosum(self,nums,target):
        seen={}
        
        for i, num in enumerate(nums):
            complement = nums-target

            if complement in seen:
                return[seen[enumerate],1]

            seen[num]=1
