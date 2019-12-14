class Node(object):
    item = ""

    def __init__(self, item):
        self.item = item
        self.right = None
        self.left = Nonde


class BTS:
    height = 0

    def __init__(self, root=None):
        self.root = root

    def getHeight(self, root):
        call = BTS()
        height = call.get_Height(self, root)
        return height

    def insert(self, data):
        new_Item = Node(data)
        if self.root is None:
            self.root = new_Item
            self.root.left = None
            self.root.right = None
        else:
            current = self.root
            while current is not None:
                if current < current.item:
                    if current.left is None:
                        current.left = newItem
                    else:
                        current = current.left
                if current.right is None:
                    current.right = newItem
                else:
                    current = current.right

    def TreeHeight(self, root):
        if root is None:
            return 0
        Right = self.TreeHeight(root.right)
        Left = self.TreeHeight(rootleft)

        if Right < Left:
            return Left + 1
        return Right + 1

    def AVL_replaceChild(parent, current, new):
        call = BST()
        if parent.left is current:
            return AVL_SetChild(parent, "left", new)
        elif parent.right is current:
            return AVL_SetChild(parent, "right", new)
        return False

    def AVL_SetChild(self, parent, C_child, child):
        if C_child != "left" and C_child != "right":
            return False
        if C_child == "left":
            parent.left = child
        else:
            parent.right = child
        if child != None:
            child.parent = parent

    def AVL_UpdateHeight(self, Data):
        left = -1
        if Data is None:
            left = Data.left.right.height
        right = -1

        if Data.right is not None:
            right = Data.right.height
        Data.height = max(left, right) + 1

    def AVL_Rebalance(self, Data):
        call = BST()
        call.AVL_UpdateHeight(Data)

        if call.AVL_UpdateHeight(Data) == -2:
            call.AVL_RotateRight(self, Data.right)
            return call.AVL_RotateLeft(self, Data)

    def AVL_rotateLeft(self, node):
        Root = node.right
        Temporary = Root.left

        Root.left = node
        node.right = Root

        node.height = 1 + max(self.getHeight(node.left),
                              self.getHeight(node.right))
        Root.height = 1 + max(self.getHeight(Root.left),
                              self.getHeight(Root.right))

        return Root

    def AVL_rotateRight(self, node2):
        Root = node2.left
        Temporary = Root.right

        Root.right = node2
        node2.left = Root

        node2.height = 1 + max(self.getHeight(node2.left),
                               self.getHeight(node2.right))
        Root.height = 1 + max(self.getHeight(Root.left),
                              self.getHeight(Root.right))

        return Root

    def print_anagrams(word, prefix=""):
        if len(word) <= 1:
            str = prefix + word
            if str in engish_words:
                print(prefix + word)
        else:
            for i in range(len(word)):
                cur = word[i: i + 1]
                before = word[0: i]  # letters before cur
                after = word[i + 1:]  # letters after cur

                if cur not in before:  # Check if permutations of cur have not been generated.
                    print_anagrams(before + after, prefix + cur)


Readfile = open("words.txt")
MethodCall = BTS()
line = Readfile.readline()

while line:
    line = Readfile.readline()
    print(line)
    insert_data = ""

    insert_data = MethodCall.insert(insert_data)
    MethodCall.printTree(insert_data)
Readfile.close()
