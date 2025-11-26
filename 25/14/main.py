import time


class Solution:
    def __init__(self, test=False):
        self.test = test

    def read_data(self, part):
        filename = f"testinput{part}.txt" if self.test else f"input{part}.txt"
        return open(filename).read()

    def get_next_state(self, data):
        new_data = []
        s = 0
        for y in range(self.R):
            new_row = ""
            for x in range(self.C):

                num_active_neighbors = 0
                for dx, dy in [(-1, -1), (1, -1), (1, 1), (-1, 1)]:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or nx >= self.C or ny < 0 or ny >= self.R:
                        continue
                    if data[ny][nx] == "#":
                        num_active_neighbors += 1

                c = data[y][x]
                if (c == "#" and num_active_neighbors % 2 == 1) or (
                    c == "." and num_active_neighbors % 2 == 0
                ):
                    s += 1
                    new_row += "#"
                else:
                    new_row += "."

            new_data.append(new_row)

        return (new_data, s)

    def part1(self):
        data = self.read_data(1).split("\n")
        self.R = len(data)
        self.C = len(data[0])

        res = 0
        for _ in range(10):
            data, s = self.get_next_state(data)
            res += s

        return res

    def part2(self):
        data = self.read_data(2).split("\n")
        self.R = len(data)
        self.C = len(data[0])

        res = 0
        for _ in range(2025):
            data, s = self.get_next_state(data)
            res += s

        return res

    def check_pattern(self, data):
        for dy in range(len(self.pattern)):
            for dx in range(len(self.pattern[dy])):
                x = 13 + dx
                y = 13 + dy
                if data[y][x] != self.pattern[dy][dx]:
                    return False

        return True

    def part3(self):
        self.pattern = self.read_data(3).split("\n")
        self.C, self.R = 34, 34

        data = ["." * self.C for _ in range(self.R)]

        cycle = []
        seen = set()
        for round in range(1000000000):
            data, s = self.get_next_state(data)

            if self.check_pattern(data):

                if tuple(data) in seen:
                    first_round = cycle[0][0]
                    cycle_length = round - first_round

                    cycle_sum = 0
                    for _, _sum in cycle:
                        cycle_sum += _sum

                    rounds_left = 1000000000 - first_round

                    num_cycles = rounds_left // cycle_length
                    res = cycle_sum * num_cycles

                    rounds_left = rounds_left % cycle_length
                    for i in range(len(cycle)):
                        if rounds_left < cycle[i][0] - first_round:
                            break
                        res += cycle[i][1]
                        rounds_left -= cycle[i][0] - first_round

                    return res

                seen.add(tuple(data))
                cycle.append((round, s))

        return res


def main():
    start = time.perf_counter()

    s = Solution(test=True)
    print("---TEST---")
    print(f"part 1: {s.part1()}")
    print(f"part 3: {s.part3()}\n")

    s = Solution()
    print("---MAIN---")
    print(f"part 1: {s.part1()}")
    print(f"part 2: {s.part2()}")
    print(f"part 3: {s.part3()}\n")

    print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")


main()
