import time
import itertools
import functools
from collections import Counter, defaultdict, deque
import networkx as nx
from tqdm import tqdm
import numpy as np
import re
import copy

import sys
sys.path.append("../..")
from utils import adjacent4, adjacent8, directions4, directions8, manhattanDist


class Node():
    def __init__(self, id, rank, symbol):
        self.id = id
        self.rank = rank
        self.symbol = symbol
        self.left = None
        self.right = None
        self.parent = None
        
class BinaryTree():
    def __init__(self):
        self.root = None
        self.nodes: dict[int, Node] = {}
        
    def insert(self, node: Node):
        self.nodes[node.id] = node
        if not self.root:
            self.root = node
            return
        current = self.root
        layer = 0
        while True:
            layer += 1
            if node.rank < current.rank:
                if not current.left:
                    current.left = node
                    node.parent = current
                    return
                current = current.left
            else:
                if not current.right:
                    current.right = node
                    node.parent = current
                    return
                current = current.right
    
    def traverse_node(self, node: Node, visited: list):
        if node:
            visited.append(node)
            self.traverse_node(node.left, visited)
            self.traverse_node(node.right, visited)

    def traverse(self):
        visited = []
        self.traverse_node(self.root, visited)
        return visited
    
    
    def get_layers(self):
        if not self.root:
            return {}

        layers = defaultdict(list)
        queue = deque([(self.root, 0)])  # (node, layer_number)

        while queue:
            node, layer = queue.popleft()
            layers[layer].append(node)

            if node.left:
                queue.append((node.left, layer + 1))
            if node.right:
                queue.append((node.right, layer + 1))

        return dict(layers)
        
        
class Solution():
    def __init__(self, test=False):
        self.test = test
        
    def read_data(self, part):
        filename = f"testinput{part}.txt" if self.test else f"input{part}.txt"
        return open(filename).read()
        
    def part1(self):
        left = BinaryTree()
        right = BinaryTree()
        data = self.read_data(1)
        pattern = re.compile(r"ADD id=(\d+) left=\[(\d+),(.)\] right=\[(\d+),(.)\]")
        for line in data.split("\n"):
            match = pattern.match(line)
            m = match.groups()
            l = Node(int(m[0]), int(m[1]), m[2])
            r = Node(int(m[0]), int(m[3]), m[4])
            left.insert(l)
            right.insert(r)
        
        most_nodes_left = max(left.get_layers().items(), key=lambda x : len(x[1]))[1]
        left_message = "".join(map(lambda x : x.symbol, sorted(most_nodes_left, key=lambda x : x.rank)))
 
        
        most_nodes_right = max(right.get_layers().items(), key=lambda x : len(x[1]))[1]
        right_message = "".join(map(lambda x : x.symbol, sorted(most_nodes_right, key=lambda x : x.rank)))
        
        return left_message + right_message
        
        
    
    def part2(self):
        left = BinaryTree()
        right = BinaryTree()
        data = self.read_data(2)
        for line in data.split("\n"):
            if line.startswith("SWAP"):
                id = int(re.findall(r"\d+", line)[0])
                # print(id)
                self.swap_node(left, right, id)
                
            
            else:   
                pattern = re.compile(r"ADD id=(\d+) left=\[(\d+),(.)\] right=\[(\d+),(.)\]")
                match = pattern.match(line)
                m = match.groups()
                l = Node(int(m[0]), int(m[1]), m[2])
                r = Node(int(m[0]), int(m[3]), m[4])
                left.insert(l)
                right.insert(r)
                
        
        left_order = left.traverse()
        # print(list(map(lambda x: x.symbol, left_order)))
        most_nodes_left = max(left.get_layers().items(), key=lambda x : len(x[1]))[1]
        left_message = "".join(map(lambda x : x.symbol, sorted(most_nodes_left, key=lambda x : left_order.index(x))))
 
        
        right_order = right.traverse()
        # print(list(map(lambda x: x.symbol, right_order)))
        most_nodes_right = max(right.get_layers().items(), key=lambda x : len(x[1]))[1]
        right_message = "".join(map(lambda x : x.symbol, sorted(most_nodes_right, key=lambda x : right_order.index(x))))
        
        return left_message + right_message
    
    def swap_node(self, left: BinaryTree, right: BinaryTree, id):
        left.nodes[id].rank, left.nodes[id].symbol, right.nodes[id].rank, right.nodes[id].symbol = right.nodes[id].rank, right.nodes[id].symbol, left.nodes[id].rank, left.nodes[id].symbol
    
    def swap(self, left: BinaryTree, right: BinaryTree, id: int):
        left_node = left.nodes[id]
        right_node = right.nodes[id]

        left_parent = left_node.parent
        right_parent = right_node.parent

        left_is_left_child = left_parent and left_parent.left == left_node
        right_is_left_child = right_parent and right_parent.left == right_node

        # Swap parents
        if left_parent:
            if left_is_left_child:
                left_parent.left = right_node
            else:
                left_parent.right = right_node
        else:
            left.root = right_node

        if right_parent:
            if right_is_left_child:
                right_parent.left = left_node
            else:
                right_parent.right = left_node
        else:
            right.root = left_node

        # Swap .parent references
        right_node.parent = left_parent
        left_node.parent = right_parent
        
        
        
        
        
    
    def part3(self):
        left = BinaryTree()
        right = BinaryTree()
        data = self.read_data(3)
        for line in data.split("\n"):
            if line.startswith("SWAP"):
                id = int(re.findall(r"\d+", line)[0])
                # print(id)
                self.swap(left, right, id)
            else:   
                pattern = re.compile(r"ADD id=(\d+) left=\[(\d+),(.)\] right=\[(\d+),(.)\]")
                match = pattern.match(line)
                m = match.groups()
                l = Node(int(m[0]), int(m[1]), m[2])
                r = Node(int(m[0]), int(m[3]), m[4])
                left.insert(l)
                right.insert(r)
                
        
        left_order = left.traverse()
        # print(list(map(lambda x: x.symbol, left_order)))
        most_nodes_left = max(left.get_layers().items(), key=lambda x : len(x[1]))[1]
        left_message = "".join(map(lambda x : x.symbol, sorted(most_nodes_left, key=lambda x : left_order.index(x))))
 
        
        right_order = right.traverse()
        # print(list(map(lambda x: x.symbol, right_order)))
        most_nodes_right = max(right.get_layers().items(), key=lambda x : len(x[1]))[1]
        right_message = "".join(map(lambda x : x.symbol, sorted(most_nodes_right, key=lambda x : right_order.index(x))))
        
        return left_message + right_message
    
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