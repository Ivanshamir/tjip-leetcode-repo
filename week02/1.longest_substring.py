# Naive Approach
# Time Complexity O(N^2) | Space Complexity O(1)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        
        string = ''
        maxSize = len(string)
        i = j = 0
        
        while i < len(s):
            j = i
            
            while j < len(s) and s[j] not in string:
                string += s[j]
                j += 1
            
            maxSize = max(maxSize, len(string))
            string = ''
            i += 1
        
        return maxSize


# Better approach
# Time Complexity O(N) | Space Complexity O(N)
"""
Description: we will use sliding window approach. For check duplicate value we are using a set. If value is already added in set then removes the left most value until all unique values are found in set. Otherwise value add in set and get max value: max(maxSize, i-left+1)
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        characterSet = set()
        left = 0
        maxSize = 0
        
        for i in range(len(s)):
            while s[i] in characterSet:
                characterSet.remove(s[left])
                left += 1
            
            characterSet.add(s[i])
            maxSize = max(maxSize, i-left+1)
        
        return maxSize