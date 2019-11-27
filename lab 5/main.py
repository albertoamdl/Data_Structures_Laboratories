from LRU import LRU
from Heaps import MaxHeap


def main(a):
    if a == 1:
        least_recently_used = LRU(3)

        least_recently_used.put("A", 0)
        least_recently_used.put("B", 1)
        least_recently_used.put("C", 2)

        least_recently_used.print_cache_dictionary()
        least_recently_used.print_cache_doubly()
        print()

        least_recently_used.get("A")
        least_recently_used.print_cache_dictionary()
        least_recently_used.print_cache_doubly()
        print()

    else:
        word_list = []
        with open("WORDS") as file:
            line = file.readline().split()
            while line:
                word_list.extend(line)
                line = file.readline().split()

        most_frequent_elements(word_list)


def most_frequent_elements(words):
    heap = MaxHeap()

    for word in words:
        heap.insert(word)

    for i in range(len(heap.tree)):
        print(str(heap.tree[i].word) + " " + str(heap.tree[i].count))


main(1)