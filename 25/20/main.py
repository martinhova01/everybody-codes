import time
from collections import deque


class Solution:
    def __init__(self, test=False):
        self.test = test

    def read_data(self, part):
        filename = f"testinput{part}.txt" if self.test else f"input{part}.txt"
        return open(filename).read().split("\n")

    def part1(self):
        data = self.read_data(1)

        s = 0

        for i in range(len(data) - 1):
            for j in range(i + 1, len(data[i]), 2):
                if data[i][j] != "T":
                    continue

                # down
                if data[i][j] == data[i + 1][j]:
                    s += 1

                # left
                if data[i][j] == data[i][j - 1]:
                    s += 1

                # right
                if data[i][j] == data[i][j + 1]:
                    s += 1

        return s

    def part2(self):
        data = self.read_data(2)

        start = None
        goal = None

        for row in range(len(data)):
            for col in range(len(data)):
                if data[row][col] == "S":
                    start = (col, row)

                if data[row][col] == "E":
                    goal = (col, row)

        visited = set()

        q = deque([(start[0], start[1], 0)])
        while q:

            x, y, step = q.popleft()

            if (x, y) == goal:
                return step

            if (x, y) in visited:
                continue

            visited.add((x, y))

            neighbors = [(-1, 0), (1, 0)]

            if (y + x) % 2 == 0:
                neighbors.append((0, -1))
            else:
                neighbors.append((0, 1))

            for dx, dy in neighbors:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= len(data[y]):
                    continue
                if ny < 0 or ny >= len(data):
                    continue

                if data[ny][nx] == "#" or data[ny][nx] == ".":
                    continue

                q.append((nx, ny, step + 1))

    def part3(self):
        _ = self.read_data(3)
        return None


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
