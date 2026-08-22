class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = []

        for i in range(len(strs[0])):
            for s in strs:
                if i >= len(s):
                    return "".join(prefix)

                if s[i] != strs[0][i]:
                    return "".join(prefix)

            prefix.append(strs[0][i])

        return "".join(prefix)