import time
from itertools import combinations
import networkx as nx


class Solution:
    def __init__(self, test=False):
        self.test = test

    def read_data(self, part):
        filename = f"testinput{part}.txt" if self.test else f"input{part}.txt"
        return open(filename).read()

    def parse(self, data):
        scales = {}
        for line in data.split("\n"):
            id, dna = line.split(":")
            id = int(id)
            scales[id] = dna
        return scales

    def is_child(self, child, par1, par2):

        for i, c in enumerate(child):
            if c != par1[i] and c != par2[i]:
                return False

        return True

    def part1(self):
        scales = self.parse(self.read_data(1))

        ids = {1, 2, 3}

        for id, child in scales.items():

            par_id1, par_id2 = ids - {id}
            par1 = scales[par_id1]
            par2 = scales[par_id2]

            if not self.is_child(child, par1, par2):
                continue

            s_1 = 0
            s_2 = 0
            for i in range(len(child)):
                if child[i] == par1[i]:
                    s_1 += 1
                if child[i] == par2[i]:
                    s_2 += 1

            return s_1 * s_2

    def part2(self):
        scales = self.parse(self.read_data(2))

        res = 0

        for id_par1, id_par2 in combinations(scales, 2):
            for id_child, child in scales.items():
                if id_child == id_par1 or id_child == id_par2:
                    continue

                if not self.is_child(child, scales[id_par1], scales[id_par2]):
                    continue

                par1 = scales[id_par1]
                par2 = scales[id_par2]

                s_1 = 0
                s_2 = 0
                for i in range(len(child)):
                    if child[i] == par1[i]:
                        s_1 += 1
                    if child[i] == par2[i]:
                        s_2 += 1

                res += s_1 * s_2
        return res

    def part3(self):
        scales = self.parse(self.read_data(3))

        G = nx.Graph()

        for id_par1, id_par2 in combinations(scales, 2):
            for id_child, child in scales.items():
                if id_child == id_par1 or id_child == id_par2:
                    continue

                if not self.is_child(child, scales[id_par1], scales[id_par2]):
                    continue

                G.add_edge(id_child, id_par1)
                G.add_edge(id_child, id_par2)

        largest_cc_nodes = max(nx.connected_components(G), key=len)
        return sum(largest_cc_nodes)


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
