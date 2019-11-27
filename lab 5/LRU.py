from DoublyNode import DoublyNode


class LRU:
    def __init__(self, max_capacity=5):
        self._cache = {}
        self._max_capacity = max_capacity
        self._count = 0
        self._tail = None
        self._head = None

    def get(self, key):
        if key in self._cache:
            desired_node = self._cache[key]

            if desired_node is self._tail or len(self._cache) == 1:
                return desired_node.value
            elif desired_node is self._head:
                temp = self._head
                self._head = self._head.next
                self._head.previous = None

                self._tail.next = temp
                self._tail = temp
                temp.next = None
            else:
                left_node = desired_node.previous
                right_node = desired_node.next

                left_node.next = right_node
                right_node.previous = left_node

                self._tail.next = desired_node
                desired_node.previous = self._tail
                self._tail = desired_node
                desired_node.next = None

            return desired_node.value
        else:
            return -1

    def put(self, key, value):
        new_doubly_node = DoublyNode(key, value)
        if self._head is None:
            self._head = new_doubly_node
            self._tail = new_doubly_node
            self._count += 1
        elif self._count < self._max_capacity:
            self._tail.next = new_doubly_node
            new_doubly_node.previous = self._tail
            self._tail = new_doubly_node
            self._count += 1
        else:
            del self._cache[self._head.key]
            self._tail.next = new_doubly_node
            new_doubly_node.previous = self._tail
            self._tail = new_doubly_node
            self._head = self._head.next
            self._head.previous = None

        self._cache[key] = new_doubly_node

    def size(self):
        return self._count

    def max_capacity(self):
        return self._max_capacity

    def print_cache_doubly(self):
        temp = self._head
        print("None <- ", end='')
        while temp is not None:
            if temp.next is None:
                print(str(temp.key), end='')
                break

            print(str(temp.key) + " <-> ", end='')
            temp = temp.next

        print(" -> None")

    def print_cache_dictionary(self):
        for key in self._cache.keys():
            print(str(key) + ": " + str(self._cache[key].value) + ", ", end='')
        print()

    def __str__(self):
        return str(self._cache)