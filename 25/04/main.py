import time
import math


class Solution:
    def __init__(self, test=False):
        self.test = test

    def read_data(self, part):
        filename = f"testinput{part}.txt" if self.test else f"input{part}.txt"
        return open(filename).read()

    def part1(self):
        data = list(map(int, self.read_data(1).split("\n")))

        res = 2025
        for i in range(1, len(data)):
            res *= data[i - 1] / data[i]

        return int(res)

    def part2(self):
        data = list(map(int, self.read_data(2).split("\n")))

        target = 10000000000000
        mult = 1
        for i in range(1, len(data)):
            mult *= data[i - 1] / data[i]

        return math.ceil(target / mult)

    def part3(self):
        data = self.read_data(3)

        gears = []
        for i, line in enumerate(data.split("\n")):
            if i == 0:
                gears.append((0, int(line)))
            else:
                gears.append(tuple(map(int, line.split("|"))))

        res = 100
        for i in range(1, len(gears)):
            res *= gears[i - 1][1] / gears[i][0]

        return res


def main():
    start = time.perf_counter()

    s = Solution(test=True)
    print("---TEST---")
    print(f"part 1: {s.part1()}")
    print(f"part 2: {s.part2()}")
    print(f"part 3: {s.part3()}\n")

    s = Solution()
    print("---MAIN---")
    print(f"part 1: {s.part1()}")
    print(f"part 2: {s.part2()}")
    print(f"part 3: {s.part3()}\n")

    print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")


main()
