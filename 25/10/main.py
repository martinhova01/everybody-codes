import time
from functools import cache
from collections import deque


class Solution:
    def __init__(self, test=False):
        self.test = test
        self.moves = [
            (-2, -1),
            (-1, -2),
            (1, -2),
            (2, -1),
            (2, 1),
            (1, 2),
            (-1, 2),
            (-2, 1),
        ]

    def read_data(self, part):
        filename = f"testinput{part}.txt" if self.test else f"input{part}.txt"
        return open(filename).read()

    def part1(self):
        data = self.read_data(1).split("\n")
        stop = 3 if self.test else 4

        visited = set()
        start_y, start_x = len(data) // 2, len(data[0]) // 2
        q = deque([(start_x, start_y, 0)])  # (x, y, step)
        hits = 0
        while q:
            x, y, step = q.popleft()

            if (x, y) in visited:
                continue

            if step > stop:
                continue

            if data[y][x] == "S":
                hits += 1

            visited.add((x, y))

            for dx, dy in self.moves:
                if (
                    x + dx < 0
                    or x + dx >= len(data[y])
                    or y + dy < 0
                    or y + dy >= len(data)
                ):
                    continue

                q.append((x + dx, y + dy, step + 1))

        return hits

    def part2(self):
        data = self.read_data(2).split("\n")
        stop = 3 if self.test else 20

        hideouts = set()
        sheep = set()
        for y in range(len(data)):
            for x in range(len(data[y])):
                c = data[y][x]
                if c == "S":
                    sheep.add((x, y))
                elif c == "#":
                    hideouts.add((x, y))

        start_sheep = len(sheep)

        visited = set()
        start_y, start_x = len(data) // 2, len(data[0]) // 2
        q = deque([(start_x, start_y, 0)])  # (x, y, step)
        while q:
            x, y, step = q.popleft()

            if (x, y, step) in visited:
                continue

            if step > stop:
                continue

            visited.add((x, y, step))

            if (x, y - step) in sheep and (x, y) not in hideouts:
                sheep.remove((x, y - step))

            if (x, y - step + 1) in sheep and (x, y) not in hideouts:
                sheep.remove((x, y - step + 1))

            for dx, dy in self.moves:
                if (
                    x + dx < 0
                    or x + dx >= len(data[y])
                    or y + dy < 0
                    or y + dy >= len(data)
                ):
                    continue

                q.append((x + dx, y + dy, step + 1))

        PRINT = False
        if PRINT:
            out = ""
            for y in range(len(data)):
                for x in range(len(data[y])):
                    if (x, y, stop) in visited:
                        out += "X"
                    else:
                        out += "."
                out += "\n"
            print(out)

        return start_sheep - len(sheep)

    # turn = 0 => sheep turn
    # turn = 1 => dragon turn
    @cache
    def num_moves(self, sheep: tuple, hideouts: tuple, dragon: tuple, turn: int):
        if not sheep:
            return 0

        s = 0
        if turn == 0:
            # sheep turn
            moved = False
            for x, y in sheep:
                if (x, y + 1) == dragon and (x, y + 1) not in hideouts:
                    continue
                moved = True

                if y + 1 == self.R:
                    s += 0

                else:
                    next_sheep = set(sheep)
                    next_sheep = next_sheep.difference({(x, y)})
                    next_sheep.add((x, y + 1))
                    s += self.num_moves(tuple(next_sheep), hideouts, dragon, 1)

            if not moved:
                s = self.num_moves(sheep, hideouts, dragon, 1)

        else:
            # dragon turn
            x, y = dragon
            for dx, dy in self.moves:
                nx, ny = x + dx, y + dy

                if nx < 0 or nx >= self.C or ny < 0 or ny >= self.R:
                    continue

                next_sheep = set(sheep)
                if (nx, ny) in sheep and (nx, ny) not in hideouts:
                    next_sheep.remove((nx, ny))
                    if not next_sheep:
                        s += 1

                s += self.num_moves(tuple(next_sheep), hideouts, (nx, ny), 0)

        return s

    def part3(self):
        data = self.read_data(3).split("\n")
        self.R = len(data)
        self.C = len(data[0])

        hideouts = set()
        sheep = set()
        dragon: tuple = None
        for y in range(len(data)):
            for x in range(len(data[y])):
                c = data[y][x]
                if c == "S":
                    sheep.add((x, y))
                elif c == "#":
                    hideouts.add((x, y))
                elif c == "D":
                    dragon = (x, y)

        return self.num_moves(tuple(sheep), tuple(hideouts), dragon, 0)


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
