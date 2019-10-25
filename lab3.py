class Node(object):
    item = ""
    height = 0

    def __init__(self,item):
       self.item = item
       self.parent = None
       self.right = None
       self.left = None
       self.color = ""



class AVL:
    count = 0
    root = None



    def __init__(self,root = None):
         self.root = root



    @staticmethod    
    def get_TreeHeight(root):     
        if root is None:
            return 0

        Lh = root.get_TreeHeight(root.left)
        Rh = root.get_TreeHeight(root.right)

        if Lh > Rh :
            return Lh + 1
        else:
            return Rh + 1




    @staticmethod        
    def AVL_Update(nodeData):
        leftH = -1
        if nodeData is not None:
            leftH = nodeData.height
        rightH = -1

        if nodeData.right is not None:

            rightH = nodeData.right.height
        nodeData.height = max(leftH,rightH) + 1    




    @staticmethod
    def getHeight(root):
        H = root.get_TreeHeight(root)
        return H




    def AVL_Rebalance(self,nodeData):
        self.AVL_Update(nodeData)

        if self.AVL_Update(nodeData) == -2:

            self.AVLtreeRotateR(nodeData.right)
            return self.AVLtreeRotateL(nodeData)   
 




    def AVL_Set(self,parent,WhichChild,child):
        if WhichChild != "left" and WhichChild != "right":
            return False
        if WhichChild == "left":
            parent.left = child
        else:
            parent.right = child
        if child != None:
            child.parent = parent
            



    def AVL_Replace(parent,currChild,newChild):
        c = AVL()

        if parent.left is currChild:
            return c.AVL_Set(parent,"left", newChild)

        elif(parent.right is currChild):
            return c.AVL_Set(parent,"right", newChild)
        return False
    


    # Rotate Right
    def AVL_RRotate(self,nodeD):
      newRoot  = nodeD.left
      temp = newRoot.right
      
      newRoot.right = nodeD
      nodeD.left = temp
      
      nodeD.height = 1 + max(self.getHeight(nodeD.left),self.getHeight(nodeD.right))
      newRoot.height = 1 + max(self.getHeight(newRoot.left),self.getHeight(newRoot.right))
      return newRoot
 


    # Left Rotate
    def AVL_LRotate(self,node):
      newRoot  = node.right
      temp = newRoot.left
      
      newRoot.left = node
      node.right = temp
      
      node.height = 1 + max(self.getHeight(node.left),self.getHeight(node.right))
      newRoot.height = 1 + max(self.getHeight(newRoot.left),self.getHeight(newRoot.right))
      return newRoot
    



    def AVLinsert(self,data):
        new = Node(data)
        if self.root is None:
            self.root = new
            self.root.left = None
            self.root.right = None
            new.height = new.height + 1
            return
        #curr = root
        new.height = new.height + 1
        currNode = self.root

        while currNode is not None:

            if new.item < currNode.item:
                if currNode.left is None:
                    currNode.left = new
                    new.parent = currNode
                    currNode = None
                else:
                    currNode = currNode.left

            else:
                if currNode.right is None:
                    currNode.right = new
                    new.parent = currNode
                    currNode = None
                else:
                    currNode = currNode.right
        new = new.parent

        while new is not None: 
            self.AVL_Rebalance(new)
            new = new.parent
      #  return self.root    
            



    def printTree(self,node):
        if node is None:
            return 
        self.printTree(node.left)
        print(node.item)



        self.printTree(node.right)



class RedBlacktree:
    root = None
    #count = 0
    height = 0
    def __init__(self,root = None):
         self.root = root
         self.color = "black"


    @staticmethod        
    def RedBlack_HieghtUpdate(nodeData):
        leftH = -1
        if nodeData is not None:
            leftH = nodeData.height
        rightH = -1
        if nodeData.right is not None:
            rightH = nodeData.right.height
        nodeData.height = max(leftH,rightH) + 1  

    # insert the item in the corresponding place

    def RBInsert(self, data):
        newItem = Node(data)
        if self.root is None:
            self.root = newItem
            self.root.color = "black"
            newItem.height = newItem.height + 1
            return

        newItem.height = newItem.height + 1
        currNode = self.root
        # while current_node is not None:
        #         if node.key < current_node.key:
        #             if current_node.left is None:
        #                 current_node.set_child("left", node)
        #                 break

        while currNode is not None:
            if newItem.item < currNode.item:
                if currNode.left is None:
                    currNode.left = newItem
                    newItem.parent = currNode
                    currNode = None
                else:
                    currNode = currNode.left
            else:
                if currNode.right is None:
                    currNode.right = newItem
                    newItem.parent = currNode
                    currNode = None
                else:
                    currNode = currNode.right
        newItem.color = "red"
        self.RedBlackB
        while newItem is not None:
            self.AVLTreeRebalance(newItem)
            newItem = newItem.parent

    #  def read_file(self):
    #     top10 = 0

    #     for word in self.word:
    #         x = 0

    #         if self.tree.search(word.lower()):
    #             x += 1

    #             for i in range(len(word)):

    #                 cur = word[i: i+1]
    #                 before = word[0:i]
    #                 after = word[i+1:]
    #                 anagram = "{}{}{}".format(after, before, cur)

    #                 if self.tree.search(anagram.lower()) and anagram.lower() != word.lower():
    #                     x += 1

    #             top10[word] = x
    #     sorted_top10 = sorted(top10.items(), key=operator.itemgetter(1))
    #     forcheck = 0
    #     # This is used to sort out the top 10 list
    #     for top in reversed(sorted_top10):

    #         forcheck += 1

    #         if forcheck == 11:

    #             break
    #         if top[1] == 1:

    #             print("{}. \"{}\" has {} anagram".format(
    #                 forcheck, top[0], top[1]))
    #         else:

    #             print("{}. \"{}\" has {} anagrams".format(
    #                 forcheck, top[0], top[1]))






    def RedBlack_Set(self,parent,WhichChild,child):
        if WhichChild != "left" and WhichChild != "right":
            return False
        if WhichChild == "left":
            parent.left = child
        else:
            parent.right = child
        if child != None:
            child.parent = parent    



            
    def RedBlack_Replace(parent,currChild,newChild):
        c = AVL()
        if parent.left is currChild:
            return c.AVL_Set(parent,"left", newChild)
        elif(parent.right is currChild):
            return c.AVL_Set(parent,"right", newChild)
        return False    


    #Rotate left
    def RedBlack_LRotate(self,nodeData):
        rightLChild = nodeData.right.left
        if nodeData.parent is None:
            self.RedBlack_Replace(nodeData.parent,nodeData,nodeData.right)
        else:
            self.root = nodeData

            self.root.parent = None 



        self.RedBlack_Set(nodeData.right,"left",nodeData)
        self.RedBlack_Set(nodeData,"right",rightLChild)     



    #Rotate Right
    def RedBlack_RRotate(self,nodeData):
        leftRChild = nodeData.left.right


        if nodeData.parent is not None:

            self.RedBlack_Replace(nodeData.parent,nodeData,nodeData.right)
        else:
            self.root = nodeData.right
            self.root.parent = None
        self.RedBlack_Set(nodeData.left,"right",nodeData)
        self.RedBlack_Set(nodeData,"left",leftRChild)
        
    


    @staticmethod
    def RedBlack_getGParent(node):
        if node.parent is None:
            return None
        return node.parent.parent


    @staticmethod
    def RedBlack_GetUncle(node):
        grandparent = None

        if node.parent is not None:

            grandparent = node.parent.parent
        if grandparent is None:

            return None
        if grandparent.left is node.parent:
            
            return grandparent.right
        else:

            return grandparent.left



    # Creates a balanced 
    def BalanceRedBlackTree(self,nodeData):
        if nodeData.parent is None:

            nodeData.color = "black"
            return
        if nodeData.parent.color == "black":

            return
        parent = nodeData.parent
        grandparent = self.RedBlack_getGParent(nodeData)


        uncle = self.RedBlack_GetUncle(nodeData)
        if uncle is not None and uncle.colot == "red":

            parent.color = uncle.color = "black"
            self.BalanceRedBlackTree(grandparent)
            return 
        if nodeData is parent.right and parent is grandparent.left:

            self.RedBlack_RRotate(parent)
            nodeData = parent
            parent = nodeData.parent
        elif nodeData is parent.left and parent is grandparent.right:

            self.RedBlack_RRotate(parent)
            nodeData = parent
            parent = nodeData
        parent.color = "black"    
        grandparent.color = "red"
        if nodeData is parent.left:

            self.RedBlack_RRotate(grandparent)
        else:

            self.RedBlack_LRotate(grandparent)    
    




# Search     
def BSTSearch(word):
  c = AVL()
  if c.root is None or c.root == word: # if the word its on root return true

      return True

  if c.root.item < word:

      return c.BSTSearch(c.root.right,word)

  return False# if not false
            
2  #print all possible combinations 
def print_anagrams(word, prefix=""):
    
    counter = 0
    if len(word) <= 1:

        str = prefix + word
        if BSTSearch(str):

            counter += 1
            print(prefix + word)
            
    else:

        for i in range(len(word)):
            
            cur = word[i: i + 1]
            before = word[0: i] # letters before cur
            after = word[i + 1:] # letters after cur 
    
            if cur not in before: # Check if cur has not been generated.

                print_anagrams(before + after, prefix + cur)
                
# AVLTreeMethod read the text file line by line and insert it to the corresponding
# tree
def AVLTreeMethod(UserInput,file,word):     
    call = AVL()                  
    line = file.readline()

    while line:

        line = file.readline()
        #root = 
        call.AVLinsert(line)
      #  call.height = call.getHeight(root)
    file.close()       
    print_anagrams(word)


# RedBlackTree reads the the text file and insert it each value in the tree 
def RedBlackTreeMethod(UserInput,file,word):

    call = RedBlacktree()
    line = file.readline()

    while line:
        line = file.readline()
        call.RBInsert(line)

    file.close()

    print_anagrams(word)

def main():
    file = open("words.txt")
    print("please choose an option:")
    print("A.AVLTree")
    print("B.RBlackTree")

#     if not tree.remove_key(30):

#     print("*** Key not found. Tree is not changed. ***")
#     print(tree)
    UserInput= input()

    word = input("input a word you want to find :")

    if UserInput == "A" or UserInput == "a":
        AVLTreeMethod(UserInput,file,word)
        
    if UserInput == "B" or UserInput == "b":
        RedBlackTreeMethod(UserInput,file,word)
        
main()
