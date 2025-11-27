import time
from networkx import DiGraph, shortest_path, path_weight
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
        data = [
            [0 if x == "@" else int(x) for x in line]
            for line in self.read_data(1).split("\n")
        ]
        ROWS = len(data)
        COLS = len(data[0])
        R = 10

        vy, vx = None, None
        for y in range(ROWS):
            for x in range(COLS):
                if data[y][x] == 0:
                    vx, vy = x, y
                    break

        s = 0
        for y in range(ROWS):
            for x in range(COLS):
                if (vx - x) ** 2 + (vy - y) ** 2 <= R**2:
                    s += data[y][x]
        return s

    def part2(self):
        data = [
            [0 if x == "@" else int(x) for x in line]
            for line in self.read_data(2).split("\n")
        ]
        ROWS = len(data)
        COLS = len(data[0])

        points = {}
        vy, vx = None, None
        for y in range(ROWS):
            for x in range(COLS):
                if data[y][x] == 0:
                    vx, vy = x, y
                else:
                    points[(x, y)] = data[y][x]

        R = 1
        res = {}
        while points:
            s = 0
            remove = set()
            for (x, y), n in points.items():
                if (vx - x) ** 2 + (vy - y) ** 2 <= R**2:
                    s += n
                    remove.add((x, y))

            for key in remove:
                del points[key]

            res[R] = s
            R += 1

        best = (0, 0)
        for r, value in res.items():
            if value > best[1]:
                best = (r, value)

        return best[0] * best[1]

    def part3(self):
        data = self.read_data(3).split("\n")
        ROWS = len(data)
        COLS = len(data[0])

        G = DiGraph()
        vy, vx = None, None
        start_x, start_y = None, None
        for y in range(ROWS):
            for x in range(COLS):
                c = data[y][x]
                if c == "@":
                    vx, vy = x, y
                if c == "S":
                    start_x, start_y = x, y

                for nx, ny in adjacent4(x, y):
                    if nx < 0 or nx >= COLS or ny < 0 or ny >= ROWS:
                        continue

                    nc = data[ny][nx]
                    if nc == "@":
                        continue

                    weight = 0
                    if nc != "S":
                        weight = int(nc)

                    G.add_edge((x, y), (nx, ny), w=weight)

        r = 0
        while True:
            r += 1
            time = (r + 1) * 30

            g = G.copy()
            for y in range(ROWS):
                for x in range(COLS):

                    c = data[y][x]
                    if c == "S" or c == "@":
                        continue

                    if (vx - x) ** 2 + (vy - y) ** 2 <= r**2:
                        g.remove_node((x, y))

            checkpoints = [
                (start_x, start_y),
                (vx - (r + 1), vy),
                (vx, vy + (r + 1)),
                (
                    vx + (r + 2),
                    vy,
                ),  # manually found that this is the optimal checkpoint
                (start_x, start_y),
            ]

            path = []
            for i in range(len(checkpoints) - 1):
                start = checkpoints[i]
                goal = checkpoints[i + 1]
                path.extend(shortest_path(g, start, goal, weight="w")[0:-1])

            path.append((start_x, start_y))

            w = path_weight(g, path, weight="w")
            if w >= time:
                continue

            # print path
            # out = ""
            # for y in range(ROWS):
            #     for x in range(COLS):
            #         if (x, y) in path:
            #             out += "#"
            #         else:
            #             out += "."
            #     out += "\n"

            return w * r


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
