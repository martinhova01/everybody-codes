import time
from collections import defaultdict


class Solution:
    def __init__(self, test=False):
        self.test = test

    def read_data(self, part):
        filename = f"testinput{part}.txt" if self.test else f"input{part}.txt"
        return open(filename).read()

    def part1(self):
        data = list(map(int, self.read_data(1).split(",")))
        self.N = 8 if self.test else 32

        s = 0
        for i in range(1, len(data)):
            if abs(data[i] - data[i - 1]) == self.N / 2:
                s += 1
        return s

    def part2(self):
        data = list(map(int, self.read_data(2).split(",")))
        self.N = 8 if self.test else 256

        U: set = set(range(1, self.N + 1))

        s = 0
        E = set()
        for i in range(1, len(data)):
            u, v = data[i], data[i - 1]

            # define cut
            left = set(range(min(u, v) + 1, max(u, v)))
            right = U - left - {u, v}

            # Count edges that cross the cut
            for e in E:
                if e[0] in left and e[1] in right or e[0] in right and e[1] in left:
                    s += 1

            E.add((u, v))

        return s

    def part3(self):
        data = list(map(int, self.read_data(3).split(",")))
        self.N = 8 if self.test else 256
        U: set = set(range(1, self.N + 1))

        E = defaultdict(int)
        for i in range(1, len(data)):
            u, v = data[i], data[i - 1]
            E[(u, v)] += 1

        # Try all cuts
        best = 0
        for u in range(1, self.N + 1):
            for v in range(1, self.N + 1):
                if u == v:
                    continue

                # Define cut
                left = set(range(min(u, v) + 1, max(u, v)))
                right = U - left - {u, v}

                # Sum weight over cut
                s = 0
                for e, w in E.items():
                    if e[0] in left and e[1] in right or e[0] in right and e[1] in left:
                        s += w
                if (u, v) in E:
                    s += E[(u, v)]

                best = max(best, s)

        return best


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
