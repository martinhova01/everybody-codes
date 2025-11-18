import time
import re


class ComplexNum:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return ComplexNum(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return ComplexNum(
            self.x * other.x - self.y * other.y, self.x * other.y + self.y * other.x
        )

    def __truediv__(self, other):
        return ComplexNum(int(self.x / other.x), int(self.y / other.y))

    def __str__(self):
        return f"[{self.x},{self.y}]"


class Solution:
    def __init__(self, test=False):
        self.test = test

    def read_data(self, part):
        filename = f"testinput{part}.txt" if self.test else f"input{part}.txt"
        return open(filename).read()

    def part1(self):
        data = self.read_data(1)
        x, y = list(map(int, re.findall(r"\d+", data)))
        A = ComplexNum(x, y)

        res = ComplexNum(0, 0)
        for _ in range(3):
            res *= res
            res /= ComplexNum(10, 10)
            res += A

        return res

    def is_valid(self, num: ComplexNum):

        res = ComplexNum(0, 0)
        for _ in range(100):
            res *= res
            res /= ComplexNum(100_000, 100_000)
            res += num
            if (
                res.x <= -1_000_000
                or res.x >= 1_000_000
                or res.y <= -1_000_000
                or res.y >= 1_000_000
            ):
                return False

        return True

    def part2(self):
        data = self.read_data(2)
        Ax, Ay = list(map(int, re.findall(r"-?\d+", data)))
        A = ComplexNum(Ax, Ay)
        B = A + ComplexNum(1000, 1000)

        points = set()
        for y in range(A.y, B.y + 1, 10):
            for x in range(A.x, B.x + 1, 10):
                if self.is_valid(ComplexNum(x, y)):
                    points.add((x, y))

        return len(points)

    def part3(self):
        data = self.read_data(3)
        Ax, Ay = list(map(int, re.findall(r"-?\d+", data)))
        A = ComplexNum(Ax, Ay)
        B = A + ComplexNum(1000, 1000)

        points = set()
        for y in range(A.y, B.y + 1):
            for x in range(A.x, B.x + 1):
                if self.is_valid(ComplexNum(x, y)):
                    points.add((x, y))

        return len(points)


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
