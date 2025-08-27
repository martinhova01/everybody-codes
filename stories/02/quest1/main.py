import time
from itertools import permutations
from functools import lru_cache


class Solution:
    def __init__(self, test=False):
        self.test = test

    def read_data(self, part):
        filename = f"testinput{part}.txt" if self.test else f"input{part}.txt"
        return open(filename).read()

    @lru_cache(maxsize=None)
    def run(self, start_slot: int, token: str) -> int:
        x, y = start_slot * 2, -1
        direction_index = 0
        while y < len(self.grid) - 1:
            below = self.grid[y + 1][x]
            if below == ".":
                y += 1
                continue
            if below == "*":
                direction = token[direction_index]
                direction_index += 1
                if direction == "L":
                    if x == 0:
                        x += 1
                    else:
                        x -= 1
                else:
                    if x == len(self.grid[y]) - 1:
                        x -= 1
                    else:
                        x += 1

        res = ((x // 2) + 1) * 2 - (start_slot + 1)
        return res if res >= 0 else 0

    def parse(self, data):
        grid = []
        tokens = []
        grid_input, tokens_input = data.split("\n\n")
        for line in grid_input.split("\n"):
            grid.append(line)

        for line in tokens_input.split("\n"):
            tokens.append(line)

        return grid, tokens

    def part1(self):
        data = self.read_data(1)
        self.grid, tokens = self.parse(data)
        s = 0
        for i, token in enumerate(tokens):
            s += self.run(i, token)
        return s

    def part2(self):
        data = self.read_data(2)
        self.grid, tokens = self.parse(data)
        slot_num = len(self.grid[0]) // 2 + 1

        s = 0
        for token in tokens:
            best = 0
            for i in range(slot_num):
                best = max(best, self.run(i, token))
            s += best
        return s

    def part3(self):
        data = self.read_data(3)
        self.grid, tokens = self.parse(data)
        slot_num = len(self.grid[0]) // 2 + 1

        worst, best = float("inf"), 0
        for comb in permutations(range(slot_num), len(tokens)):
            s = 0
            for i in range(len(tokens)):
                s += self.run(comb[i], tokens[i])

            worst = min(worst, s)
            best = max(best, s)

        return f"{worst} {best}"


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

    print(f"\nTotal time: {time.perf_counter() - start: .4f} sec")


main()
