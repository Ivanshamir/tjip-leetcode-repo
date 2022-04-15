# Time Complexity: O(N) | memory: O(1)

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        
        if not s:
            return 0
        
        result, limit, negative = 0, 2147483648, False
        
        if s[0] == '-': 
            negative = True
        elif s[0] == '+': 
            negative = False
        elif not s[0].isnumeric(): 
            return 0
        else: 
            result = ord(s[0]) - ord('0')

        for ch in range(1, len(s)):
            if s[ch].isnumeric():
                result = result*10 + (ord(s[ch]) - ord('0'))
                
                if not negative and result >= limit:
                    return limit-1
                elif negative and result >= limit:
                    return -limit
            else:
                break
    
        return result if negative == False else -result