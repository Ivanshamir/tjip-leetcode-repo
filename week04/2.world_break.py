# O(N*M*N) time, where N is the length of s, M is the length of worldDict and as we match the every world of dict so we need another N | O(1) space
"""
Description: We are using DP solution with bottom-up approach. We are looking by the worldDict with every character of s. 
"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        rslt = [False] * (len(s)+1)
        rslt[len(s)] = True
        
        for i in range(len(s)-1, -1, -1):
            for world in wordDict:
                if (i+len(world)) <= len(s)+1 and s[i:i+len(world)] == world:
                    rslt[i] = rslt[i+len(world)]
                
                if rslt[i]: #if match happens, then we do not need to match with other world
                    break
                   
        return rslt[0]