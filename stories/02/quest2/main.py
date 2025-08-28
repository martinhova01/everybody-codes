import time
from itertools import permutations, cycle
from functools import lru_cache
from collections import Counter, defaultdict, deque


class Solution:
    def __init__(self, test=False):
        self.test = test

    def read_data(self, part):
        filename = f"testinput{part}.txt" if self.test else f"input{part}.txt"
        return deque(open(filename).read())

    def part1(self):
        color_cycle = cycle("RGB")
        data = self.read_data(1)
        i = 0
        while data:
            i += 1
            color = next(color_cycle)
            while color == data[0]:
                data.popleft()
                if not data:
                    return i
            data.popleft()
        
        return i
    
    def circle_pop(self, repeat, data: str):
        data = data * repeat
        color_cycle = cycle("RGB")
        i = 0
        while data:
            if i % 100 == 0:
                print(i, len(data))
            i += 1
            color = next(color_cycle)
            if len(data) % 2 == 0:
                if data[0] == color:
                    data = data[0 : len(data) // 2] + data[len(data) // 2 + 1 :]
            data = data[1:]
        
        return i
                

    def part2(self):
        data = list(self.read_data(2))
        return self.circle_pop(100, data)

    def part3(self):
        data = list(self.read_data(3))
        return self.circle_pop(100000, data)


def main():
    start = time.perf_counter()

    s = Solution(test=True)
    print("---TEST---")
    print(f"part 1: {s.part1()}")
    print(f"part 2: {s.part2()}")
    # print(f"part 3: {s.part3()}\n")

    s = Solution()
    print("---MAIN---")
    print(f"part 1: {s.part1()}")
    print(f"part 2: {s.part2()}")
    print(f"part 3: {s.part3()}\n")

    print(f"\nTotal time: {time.perf_counter() - start: .4f} sec")


main()
