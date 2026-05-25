class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        mini = 1000000
        for i in range(len(strs)):
            mini = min(mini, len(strs[i]))
        for i in range(mini):
            for j in range(len(strs)):
                if strs[j][i] != strs[0][i]:
                    return ans
            ans += strs[0][i]
        return ans