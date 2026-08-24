class Solution:
    def isPalindrome(self,string):
        left=0
        right=len(string)-1

        while left < right :

            while left < right and not string[left].isalnum():
                left=left+1

            while left < right and not string[right].isalnum():
                right= right-1

            if string[left].lower() != string[right].lower():
                return False
            
            left = left+1
            right=right-1
            
        return True