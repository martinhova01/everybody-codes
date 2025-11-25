import time
from collections import deque

import sys

sys.path.append("../..")
from utils import adjacent4


class Solution:
    def __init__(self, test=False):
        self.test = test

    def read_data(self, part):
        filename = f"testinput{part}.txt" if self.test else f"input{part}.txt"
        return open(filename).read()

    def part1(self):
        data = [[int(c) for c in line] for line in self.read_data(1).split("\n")]
        self.R = len(data)
        self.C = len(data[0])

        visited = set()
        q = deque([(0, 0)])
        while q:
            x, y = q.popleft()
            if (x, y) in visited:
                continue

            visited.add((x, y))

            for nx, ny in adjacent4(x, y):
                if nx < 0 or nx >= self.C or ny < 0 or ny >= self.R:
                    continue

                if data[ny][nx] <= data[y][x]:
                    q.append((nx, ny))

        return len(visited)

    def part2(self):
        data = [[int(c) for c in line] for line in self.read_data(2).split("\n")]
        self.R = len(data)
        self.C = len(data[0])

        visited = set()
        q = deque([(0, 0), (self.C - 1, self.R - 1)])
        while q:
            x, y = q.popleft()
            if (x, y) in visited:
                continue

            visited.add((x, y))

            for nx, ny in adjacent4(x, y):
                if nx < 0 or nx >= self.C or ny < 0 or ny >= self.R:
                    continue

                if data[ny][nx] <= data[y][x]:
                    q.append((nx, ny))

        return len(visited)

    def bfs(self, start_x, start_y):
        visited = set()
        q = deque([(start_x, start_y)])
        while q:
            x, y = q.popleft()
            if (x, y) in visited:
                continue

            if (x, y) in self.done:
                continue

            visited.add((x, y))

            for nx, ny in adjacent4(x, y):
                if nx < 0 or nx >= self.C or ny < 0 or ny >= self.R:
                    continue

                if self.data[ny][nx] <= self.data[y][x]:
                    q.append((nx, ny))

        return visited

    def part3(self):
        self.data = [[int(c) for c in line] for line in self.read_data(3).split("\n")]
        self.R = len(self.data)
        self.C = len(self.data[0])

        self.done = set()
        for _ in range(3):

            components = []
            for y in range(self.R):
                for x in range(self.C):
                    if (x, y) in self.done:
                        continue
                    components.append(self.bfs(x, y))

            self.done.update(sorted(components, reverse=True, key=len)[0])

        return len(self.done)


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
