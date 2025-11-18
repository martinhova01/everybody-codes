import time
from collections import Counter


class Solution:
    def __init__(self, test=False):
        self.test = test

    def read_data(self, part):
        filename = f"testinput{part}.txt" if self.test else f"input{part}.txt"
        return open(filename).read()

    def part1(self):
        data = list(reversed(sorted(map(int, self.read_data(1).split(",")))))

        curr = data[0]
        s = curr
        for num in data[1:]:
            if num < curr:
                s += num
                curr = num

        return s

    def part2(self):
        data = list(sorted(map(int, self.read_data(2).split(","))))

        curr = data[0]
        s = curr
        c = 1
        for num in data[1:]:
            if c == 20:
                break
            if num > curr:
                c += 1
                s += num
                curr = num

        return s

    def part3(self):
        data = list(map(int, self.read_data(3).split(",")))
        counts = Counter(data)
        _, top_count = counts.most_common(1)[0]
        return top_count


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
