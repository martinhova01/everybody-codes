import time
from collections import deque


class Solution:
    def __init__(self, test=False):
        self.test = test

    def read_data(self, part):
        filename = f"testinput{part}.txt" if self.test else f"input{part}.txt"
        return open(filename).read()

    def part1(self):
        data = list(map(int, self.read_data(1).split("\n")))
        l = deque([1])
        for i in range(0, len(data), 2):
            l.append(data[i])

        for i in range(1, len(data), 2):
            l.appendleft(data[i])

        i = l.index(1)
        i = (i + 2025) % len(l)
        return l[i]

    def parse_line(self, line: str):
        return tuple(map(int, line.split("-")))

    def part2(self):
        data = [self.parse_line(line) for line in self.read_data(2).split("\n")]
        l = deque([range(1, 2)])
        for i in range(0, len(data), 2):
            l.append(range(data[i][0], data[i][1] + 1))

        for i in range(1, len(data), 2):
            l.appendleft(range(data[i][1], data[i][0] - 1, -1))

        i = l.index(range(1, 2))
        turns = 20252025
        while turns > 0:
            r = l[i]
            if len(r) > turns:
                return r.start + r.step * turns

            turns -= len(r)
            i = (i + 1) % len(l)

        return l[i].start

    def part3(self):
        data = [self.parse_line(line) for line in self.read_data(3).split("\n")]
        l = deque([range(1, 2)])
        for i in range(0, len(data), 2):
            l.append(range(data[i][0], data[i][1] + 1))

        for i in range(1, len(data), 2):
            l.appendleft(range(data[i][1], data[i][0] - 1, -1))

        i = l.index(range(1, 2))
        turns = 202520252025
        while turns > 0:
            r = l[i]
            if len(r) > turns:
                return r.start + r.step * turns

            turns -= len(r)
            i = (i + 1) % len(l)

        return l[i].start


def main():
    start = time.perf_counter()

    s = Solution(test=True)
    print("---TEST---")
    print(f"part 1: {s.part1()}")
    print(f"part 2: {s.part2()}")

    s = Solution()
    print("---MAIN---")
    print(f"part 1: {s.part1()}")
    print(f"part 2: {s.part2()}")
    print(f"part 3: {s.part3()}\n")

    print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")


main()
