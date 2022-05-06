# Naive approach
# time complexity O(N^2) | space O(1)

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0
        
        haystackLen = len(haystack)
        needleLen = len(needle)
        
        for i in range(haystackLen-needleLen+1):
            if haystack[i:i+needleLen] == needle:
                return i
        return -1


# Using KMP algorithm
# time complexity O(M+N) | space O(N)
"""
Description:First we need to store the length of a portion of string(needle) which is prefix and also suffix. In lps 1st position will always be 0. We will use 2 pointers approach(Example: prevlps, i). If 2nd index str is similar to 1st then increment 1 so [0,1]. If not then: if prevlps == 0 then increment i otherwise prevlps will be lps[prevlps-1].
Now going to the main part. In here we will also use two pointers: one for haystack, one for needle. If haystack[i] == needle[j] then increment by 1 in both i and j. If not then: if j=0 then incremnt i by 1 otherwise j = lps[j-1]
"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "": return 0
        
        lps = [0] * len(needle)
        prevLps = 0
        i = 1
        
        while i < len(needle):
            if needle[i] == needle[prevLps]:
                lps[i] = prevLps+1
                prevLps, i = prevLps+1, i+1
            elif prevLps == 0:
                lps[i] = 0
                i += 1
            else:
                prevLps = lps[prevLps-1]

        i = j = 0
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i,j = i+1,j+1
            else:
                if j == 0:
                    i += 1
                else:
                    j = lps[j-1]
                    
            if j == len(needle):
                return i - len(needle)
        return -1
            
        
#Using hash
class Solution:
    preCalculateHash = defaultdict(int)
    po = defaultdict(int)
    base = 29
    MOD = 1000000007
    
    def preProcess(self, haystack) -> None:
        self.preCalculateHash[0] = ord(haystack[0])
        self.po[0] = 1
        for i in range(1, len(haystack)):
            self.preCalculateHash[i] = (self.preCalculateHash[i-1] * self.base) + ord(haystack[i])
            if self.preCalculateHash[i] >= self.MOD:
                self.preCalculateHash[i] %= self.MOD

            self.po[i] = (self.po[i-1] * self.base) % self.MOD
        
    
    def getRangeHash(self, left, right):
        x1 = self.preCalculateHash[right]
        x2 = 0 if left == 0 else (self.preCalculateHash[left-1] * self.po[right-left+1]) % self.MOD
        return (x1 - x2 + self.MOD) % self.MOD
    
    
    def generateHash(self, string):
        val = 0
        for st in range(len(string)):
            val = (val * self.base) + ord(string[st])
            val %= self.MOD
            
        return val
            
    
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0
        
        haystackLen = len(haystack)
        needleLen = len(needle)
        
        self.preProcess(haystack)
        needleHash = self.generateHash(needle)
        
        for i in range(haystackLen-needleLen+1):
            if self.getRangeHash(i, i+needleLen-1) == needleHash:
                return i
        return -1