import time
import numpy as np


class Solution():
    def __init__(self, test=False):
        self.test = test
        
    def read_data(self, part):
        filename = f"testinput{part}.txt" if self.test else f"input{part}.txt"
        return open(filename).read()
        
    def part1(self):
        data = list(map(int, self.read_data(1).rstrip().split("\n")))
        data = sorted(data)
        target = data[0]
        res = 0
        for nail in data[1:]:
            res += nail - target
        return res
    
    def part2(self):
        data = list(map(int, self.read_data(2).rstrip().split("\n")))
        data = sorted(data)
        target = data[0]
        res = 0
        for nail in data[1:]:
            res += nail - target
        return res
    
    def part3(self):
        data = list(map(int, self.read_data(3).rstrip().split("\n")))
        data = sorted(data)
        m = int(np.mean(data))
        
        res = float("inf")
        
        # search around the mean value
        for target in range(m - 100000, m + 100000):
            s = 0
            for nail in data:
                s += abs(nail - target)
            res = min(res, s)
        
        return res
    
def main():
    start = time.perf_counter()
    
    s = Solution(test=True)
    print("---TEST---")
    print(f"part 1: {s.part1()}")
    # print(f"part 2: {s.part2()}")
    print(f"part 3: {s.part3()}\n")
    
    s = Solution()
    print("---MAIN---")
    print(f"part 1: {s.part1()}")
    print(f"part 2: {s.part2()}")
    print(f"part 3: {s.part3()}\n")
    
    print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")
    
main()