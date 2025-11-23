import time


class Solution:
    def __init__(self, test=False):
        self.test = test

    def read_data(self, part):
        filename = f"testinput{part}.txt" if self.test else f"input{part}.txt"
        return open(filename).read()

    def part1(self):
        data = [c for c in self.read_data(1) if c in ("A, a")]

        s = 0
        for i, c in enumerate(data):
            if c != "a":
                continue

            j = i - 1
            while j >= 0:
                if data[j] == "A":
                    s += 1
                j -= 1

        return s

    def part2(self):
        data: str = self.read_data(2)

        s = 0
        for i, c in enumerate(data):
            if c.isupper():
                continue

            j = i - 1
            while j >= 0:
                if data[j] == c.upper():
                    s += 1
                j -= 1

        return s

    def part3(self):
        data = self.read_data(3) * 1000

        s = 0
        for i, c in enumerate(data):
            if c.isupper():
                continue

            j = i - 1
            while j >= 0 and i - j <= 1000:
                if data[j] == c.upper():
                    s += 1
                j -= 1

            j = i + 1
            while j < len(data) - 1 and j - i <= 1000:
                if data[j] == c.upper():
                    s += 1
                j += 1

        return s


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
