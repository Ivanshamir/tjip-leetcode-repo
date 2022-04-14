#Time complexity: O(M.N) where M is the total chracter of first element and N is the total elements of array | Space Complexity: O(1)

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        
        for i in range(len(strs[0])):
            for st in strs:
                if i == len(st) or st[i] != strs[0][i]:
                    return result
                
            result += strs[0][i]
        
        return result