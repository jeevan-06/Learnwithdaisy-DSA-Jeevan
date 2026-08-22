class Solution:
    def isVerify(self,s):
        stack=[]
        pairs={"(":")","[":"]","{":"}"}
        
        for char in s:
            if char in "([{":
                stack.append(char)
            else:
                return False
            if pairs[stack[-1]] == char:
                stack.pop()
            if pairs[stack[-1]] != char:
                return False
        return not stack
