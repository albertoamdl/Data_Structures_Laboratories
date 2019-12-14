import collections

# This is all I have for now, I'm just working on reading the file and storing it in a list. After that, everything should be simple


class Node(object):
    item = -1
    next = None

    def __init__(self, item, next):
        self.item = item
        self.next = next

    def addNode(self, data):
        newNode = Node(data, self.head)
        self.head = newNode
        self.size += 1
        return True

    


def main():

    def BubbleSort(head, n):
        temp = head
        if (n == 1):
         return n

        # // One pass of bubble sort. After
        # // this pass, the largest element
        # // is moved(or bubbled) to end.

        for i in n-1:
            if (temp > temp.next):
                tmp = temp
                temp = temp.next
                temp.next = temp

        BubbleSort(temp, n-1)  # Traverse through remaining array



    head = Node(None, None)

    fh = open('vivendi2 .txt', 'r')
    ft = open('activision.txt', 'r')

    while fh.readline() != None:
        tmpID = fh.readline()
        tmpNode = Node(tmpID, None)
        # print(tmpID)
        tmpNode.next = head
        head = tmpNode

    while head.next != None:
        temp = head.next
        print(temp)
        temp = temp.next


        # SOLUTION 1
        temp = head
    while head.next != None:
        while temp != head.next.next:
            temp = temp.next
         
    # SOLUTION 2
    BubbleSort(temp, )




main()
