import math
from HeapNode import HeapNode


class MaxHeap(object):

    def __init__(self):
        self.tree = []
        self._word_set = set()

    def left_child(self, i):
        if 2 * i + 1 >= len(self.tree):
            return -math.inf

        return self.tree[2 * i + 1]

    def right_child(self, i):
        if 2 * i + 2 >= len(self.tree):
            return -math.inf

        return self.tree[2 * i + 2]

    def insert(self, word):
        if word in self._word_set:
            for i in range(len(self.tree)):
                if self.tree[i].word == word:
                    self.tree[i].count += 1
                    self._percolate_up(i)
        else:
            heap_node = HeapNode(word)
            self._word_set.add(word)
            self.tree.append(heap_node)
            self._percolate_up(len(self.tree) - 1)

    def _percolate_up(self, i):
        if i == 0:
            return

        parent_index = (i - 1) // 2

        parent_node = self.tree[parent_index]
        child_node = self.tree[i]

        if parent_node.count < child_node.count:
            self.tree[i], self.tree[parent_index] = self.tree[parent_index], self.tree[i]
            self._percolate_up(parent_index)

        elif parent_node.count == child_node.count and parent_node.word < child_node.word:
            self.tree[i], self.tree[parent_index] = self.tree[parent_index], self.tree[i]
            self._percolate_up(parent_index)

    def __str__(self):
        return str(self.tree)