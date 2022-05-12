# O(N) time | O(N) space complexity
"""
Details: Trie, which is also known as “Prefix Trees”, is a tree-like data structure which proves to be quite efficient for solving problems related to strings. It provides fast retrieval, and is mostly used for searching words in a dictionary, providing auto suggestions in a search engine, and even for IP routing.
"""

class TrieNode:
    def __init__(self):
        self.child = [None] * 26
        self.isWord = False

class Trie:

    def __init__(self):
        self.root = self.getNode()
        
    def getNode(self):
        return TrieNode()

    def strToIndex(self, ch):
        return ord(ch) - ord('a')

    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            index = self.strToIndex(ch)
            
            if not curr.child[index]:
                curr.child[index] = self.getNode()
            curr = curr.child[index]
                
        curr.isWord = True

    def search(self, word: str, prefixSearch=False) -> bool:
        curr = self.root
        
        for ch in word:
            index = self.strToIndex(ch)
            
            if not curr.child[index]:
                return False
            curr = curr.child[index]
            
        return curr.isWord or prefixSearch

    def startsWith(self, prefix: str) -> bool:
        return self.search(prefix, True)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)