class Node(object):

    def __init__(self, t):
        self.keys = []
        self.children = []
        self.leaf = True
        # t is the order of the parent B-Tree. Nodes need this value to define max size and splitting.
        self._t = t

    def split(self, parent, payload):
        """Split a node and reassign keys/children."""
        new_node = self.__class__(self._t)

        mid_point = self.size//2
        split_value = self.keys[mid_point]
        parent.add_key(split_value)

        # Add keys and children to appropriate nodes
        new_node.children = self.children[mid_point + 1:]
        self.children = self.children[:mid_point + 1]
        new_node.keys = self.keys[mid_point+1:]
        self.keys = self.keys[:mid_point]

        # If the new_node has children, set it as internal node
        if len(new_node.children) > 0:
            new_node.leaf = False

        parent.children = parent.add_child(new_node)
        if payload < split_value:
            return self
        else:
            return new_node

    @property
    def _is_full(self):
        return self.size == 2 * self._t - 1

    @property
    def size(self):
        return len(self.keys)

    def add_key(self, value):
        """Add a key to a node. The node will have room for the key by definition."""
        self.keys.append(value)
        self.keys.sort()

    def add_child(self, new_node):
        """
        Add a child to a node. This will sort the node's children, allowing for children
        to be ordered even after middle nodes are split.
        returns: an order list of child nodes
        """
        i = len(self.children) - 1
        while i >= 0 and self.children[i].keys[0] > new_node.keys[0]:
            i -= 1
        return self.children[:i + 1] + [new_node] + self.children[i + 1:]


class BTree(object):

    # Got help from TA

    def __init__(self, root):

        self.root = root

    def insert(self, payload):
        node = self.root

        if node._is_full:
            new_root = self.Node(self._t)
            new_root.children.append(self.root)
            new_root.leaf = False

            # node is being set to the node containing the ranges we want for payload insertion.
            node = node.split(new_root, payload)
            self.root = new_root
        while not node.leaf:
            i = node.size - 1
            while i > 0 and payload < node.keys[i]:
                i -= 1
            if payload > node.keys[i]:
                i += 1

            next = node.children[i]
            if next._is_full:
                node = next.split(node, payload)
            else:
                node = next
        # Since we split all full nodes on the way down, we can simply insert the payload in the leaf.
        node.add_key(payload)

    def search(self, value, node=None):
        if node is None:
            node = self.root
        if value in node.keys:
            return True
        elif node.leaf:
            # If we are in a leaf, there is no more to check.
            return False
        else:
            i = 0
            while i < node.size and value > node.keys[i]:
                i += 1
            return self.search(value, node.children[i])

    def print_order(self):
        this_level = self.root

        while this_level:
            next_level = None
            output = ""

            for node in this_level:
                if node.children:
                    next_level.extend(node.children)
                output += str(node.keys) + " "
            print(output)
            this_level = next_level

    def print_anagrams(word, prefix=""):

        counter = 0
        if len(word) <= 1:

            str = prefix + word
            if search(str):

                counter += 1
                print(prefix + word)

        else:

            for i in range(len(word)):

                cur = word[i: i + 1]
                before = word[0: i]  # letters before cur
                after = word[i + 1:]  # letters after cur

                if cur not in before:  # Check if cur has not been generated.

                    print_anagrams(before + after, prefix + cur)

    def print_d(self, space, node=None):
        if node is None:
            node = self.root
        # Prints keys and structure of B-tree
        if node.is_leaf:
            for i in range(len(node.keys) - 1, -1, -1):
                print(space, node.keys[i])
        else:
            self.print_d(space + '   ', node.children[len(node.keys)])
            for i in range(len(node.keys) - 1, -1, -1):
                print(space, node.keys[i])
                self.print_d(space + '   ', node.children[i])


def main():
    tree = BTree(root=3)

    nums = [6, 3, 16, 11, 7, 17, 14, 8, 5, 19,
            15, 1, 2, 4, 18, 13, 9, 20, 10, 12, 21]

    for num in nums:
        tree.insert(num)
        tree.draw()

    print('Keys in the tree: ')
    tree.print()
    print()

    print('Tree structure')
    tree.print_d('')


if __name__ == "__main__":

    main()
