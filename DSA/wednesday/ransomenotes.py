class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        count = {}

        # Count characters in magazine
        for char in magazine:
            if char in count:
                count[char] = count[char] + 1
            else:
                count[char] = 1

        # Check ransomNote characters
        for char in ransomNote:
            if char not in count or count[char] == 0:
                return False

            count[char] = count[char] - 1

        return True