class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        hashmap = {}
        for i in range(len(strs)):
            if ''.join(sorted(strs[i])) not in hashmap:
                hashmap[''.join(sorted(strs[i]))] = [strs[i]]
            else:
                hashmap[''.join(sorted(strs[i]))].append(strs[i])
        for key in hashmap:
            value = hashmap[key]
            ans.append(value)
        return ans