class slotion:
    def twosum(self):
        nums=[3,8,5,4,1]
        target=9

        seen={}
        for i,num in enumerate(nums):
            complement=target-num

            if complement in seen:
                return [seen[complement], i]
            seen[num]=i

print("Result:", slotion().twosum())