import time
from collections import Counter

class Solution():
    def __init__(self, test=False):
        self.test = test
        self.values = {"A": 0, "B": 1, "C": 3, "D": 5, "x": 0}
        
    def read_data(self, part):
        filename = f"testinput{part}.txt" if self.test else f"input{part}.txt"
        return open(filename).read()
        
    def part1(self):
        data = self.read_data(1)
        return sum(self.values[c] for c in data)
    
    def part2(self):
        data = self.read_data(2)
        s = 0
        for i in range(0, len(data) - 1, 2):
            pair = data[i : i + 2]
            if "x" not in pair:
                s += 2
            s += sum(self.values[pair[i]] for i in range(2))
        return s
    
    def part3(self):
        data = self.read_data(3)
        s = 0
        for i in range(0, len(data) - 1, 3):
            triplet = data[i : i + 3]
            count = Counter(triplet)["x"]
            if count == 0:
                s += 6
            elif count == 1:
                s += 2
            s += sum(self.values[triplet[i]] for i in range(3))
        return s
            
    
    
def main():
    start = time.perf_counter()
    
    s = Solution(test=True)
    print("---TEST---")
    print(f"part 1: {s.part1()}")
    print(f"part 2: {s.part2()}")
    print(f"part 2: {s.part3()}\n")
    
    s = Solution()
    print("---MAIN---")
    print(f"part 1: {s.part1()}")
    print(f"part 2: {s.part2()}")
    print(f"part 2: {s.part3()}")
    
    print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")
    
main()