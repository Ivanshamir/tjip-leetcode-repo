"""
Complexity: O(N) time | O(1) space

Description: The square: x4y2 ------ x2y2
                            |        /  |
                            |       /   |
                            |      /    |
                            |     /     |
                        x4y4  ------ x2y4
The main trick is that first we need to calculate the difference of points diagonally. If we found that these points are not same and there is an equal difference between abs(x2-x4) and abs(y2-y4) then we need to find x4y2 and x2y4 exists in hashmap(dictionary). When we add point then we calculate the hash and save that in hashmap. Hash formula for this problem: (x * self.BASE) + y where BASE = max prime number as possible: 1000000007
"""

class DetectSquares:

    def __init__(self):
        self.points = defaultdict(int)
        self.BASE = 1000000007
        
    def getHashedVal(self, x, y): 
        return (x * self.BASE) + y
        

    def add(self, point: List[int]) -> None:
        x,y = point
        self.points[self.getHashedVal(x,y)] += 1
        

    def count(self, point: List[int]) -> int:
        total = 0
        x2,y2 = point

        for pnt in list(self.points):
            x4 = int(pnt / self.BASE)
            y4 = pnt % self.BASE

            if (abs(x2-x4) != abs(y2-y4)) or x2 == x4:
                continue

            total +=  (self.points[self.getHashedVal(x4,y2)] * self.points[self.getHashedVal(x2,y4)] * self.points[pnt])
            
        return total
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)