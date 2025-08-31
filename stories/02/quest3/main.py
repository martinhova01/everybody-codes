import time
from collections import deque, defaultdict
import re


class Die:
    def __init__(self, id: int, faces: list[int], seed: int):
        self.id = id
        self.faces = faces
        self.seed = seed
        self.pulse = seed
        self.roll_number = 1
        self.current_face = 0

    def roll(self) -> int:
        spin = self.roll_number * self.pulse
        self.current_face = (self.current_face + spin) % len(self.faces)

        self.pulse += spin
        self.pulse %= self.seed
        self.pulse = self.pulse + 1 + self.roll_number + self.seed

        self.roll_number += 1
        return self.faces[self.current_face]

    def __str__(self):
        return f"Dice({self.id} {self.faces} {self.seed})"

    def __repr__(self):
        return self.__str__()


class Solution:
    def __init__(self, test=False):
        self.test = test

    def read_data(self, part):
        filename = f"testinput{part}.txt" if self.test else f"input{part}.txt"
        return open(filename).read()

    def parse_dice(self, input):
        dice: dict[int, Die] = {}
        for line in input.split("\n"):
            nums = list(map(int, re.findall(r"-?\d+", line)))
            id = nums[0]
            seed = nums[-1]
            faces = nums[1:-1]
            dice[id] = Die(id, faces, seed)
        return dice

    def part1(self):
        data = self.read_data(1)
        dice = self.parse_dice(data)

        s = 0
        i = 0
        while True:
            i += 1
            for die in dice.values():
                s += die.roll()
                if s >= 10000:
                    return i

    def part2(self):
        data = self.read_data(2)
        dice_input, track = data.split("\n\n")
        track = [int(elem) for elem in track]
        dice = self.parse_dice(dice_input)
        positions = {id: 0 for id in dice.keys()}

        finished = []
        while len(finished) < len(dice):
            for id, die in dice.items():
                if id in finished:
                    continue

                num = die.roll()
                if num == track[positions[id]]:
                    positions[id] += 1
                    if positions[id] == len(track):
                        finished.append(id)

        return ",".join(map(str, finished))

    def roll(self, id, roll_nr):
        if len(self.rolls[id]) < roll_nr + 1:
            self.rolls[id].append(self.dice[id].roll())
        return self.rolls[id][roll_nr]

    def part3(self):
        data = self.read_data(3)
        dice_input, board_input = data.split("\n\n")
        self.dice = self.parse_dice(dice_input)
        board = [[int(elem) for elem in line] for line in board_input.split("\n")]
        self.rolls = defaultdict(list)

        visited = set()  # (x, y, id, roll_nr)
        coins_collected = set()  # x, y
        q = deque()  # (x, y, dice_id, roll_nr)

        for y in range(len(board)):
            for x in range(len(board[y])):
                for id in self.dice.keys():
                    q.append((x, y, id, 0))

        while q:
            x, y, id, roll_nr = q.popleft()

            if (x, y, id, roll_nr) in visited:
                continue

            visited.add((x, y, id, roll_nr))

            num = self.roll(id, roll_nr)
            if num == board[y][x]:
                for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0), (0, 0)]:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or nx >= len(board[y]) or ny < 0 or ny >= len(board):
                        continue
                    coins_collected.add((x, y))
                    q.append((nx, ny, id, roll_nr + 1))

        return len(coins_collected)


def main():
    start = time.perf_counter()

    s = Solution(test=True)
    print("---TEST---")
    print(f"part 1: {s.part1()}")
    print(f"part 2: {s.part2()}")
    print(f"part 3: {s.part3()}")

    s = Solution()
    print("---MAIN---")
    print(f"part 1: {s.part1()}")
    print(f"part 2: {s.part2()}")
    print(f"part 3: {s.part3()}\n")

    print(f"\nTotal time: {time.perf_counter() - start: .4f} sec")


main()
