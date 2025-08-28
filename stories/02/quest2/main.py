import time
from itertools import cycle
from collections import deque


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

    def circle_pop(self, repeat, data: list[str]):
        data = data * repeat
        first = deque(data[0 : len(data) // 2])
        last = deque(data[len(data) // 2 :])
        color_cycle = cycle("RGB")
        i = 0
        while len(first) + len(last):
            i += 1
            color = next(color_cycle)

            # two pops
            if (len(first) + len(last)) % 2 == 0 and first[0] == color:
                last.popleft()
                first.popleft()

            # one pop
            else:
                if (len(first) + len(last)) % 2 != 0:
                    first.append(last.popleft())
                first.popleft()

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

    s = Solution()
    print("---MAIN---")
    print(f"part 1: {s.part1()}")
    print(f"part 2: {s.part2()}")
    print(f"part 3: {s.part3()}\n")

    print(f"\nTotal time: {time.perf_counter() - start: .4f} sec")


main()
