# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 10:33:48 2019

@author: LizethCampos01
"""

class Node(object):
    item = ""
    height = 0
    
    def __init__(self,item):
        self.item = item
        self.right = None
        self.left = None
        self.parent = None
        self.color = ""
class AVL:
     #height = 0
     def __init__(self,root = None):
         self.root = root
         
     def getHeight(self,root):          #getting height of tree
         call = AVL()
         height = call.get_Height(self,root)
         return height
     
     def insert(self, data):        #inserting data into the tree
         new_item = Node(data)
         if self.root is None:
                self.root = new_item
                self.root.left = None
                self.root.right = None
                new_item.height = new_item.height + 1
                return
         new_item.height = new_item.height + 1
         current = self.root
         while current is not None:
             if current.item < current.item:
                 if current.left is None:
                     current.left = new_item
                 else:
                     current = current.left
             else:              
                  if current.right is None:
                        current.right = new_item
                        new_item.parent = current
                        current = None
                  else:
                        current = current.right
         new_item = new_item.parent
         while new_item is not None: 
            self.AVL_Rebalance(new_item)
            new_item = new_item.parent
                 
     def TreeHeight(self, root):
        if root is None:
            return 0
        Right = self.TreeHeight(root.right)
        Left = self.TreeHeight(root.left)
        
        if Right < Left:
            return Left + 1
        return Right + 1
    
     def AVL_replaceChild(parent, current, new):
         call = AVL()
         if parent.left is current:
             return call.AVL_SetChild(parent, "left", new)
         elif parent.right is current:
             return call.AVL_SetChild(parent, "right", new)
         return False
     
     def AVL_SetChild(self, parent,C_child, child):
        if C_child != "left" and C_child != "right":
             return False
        if C_child == "left":
             parent.left = child
        else:
            parent.right = child
        if child != None:
            child.parent = parent
     @staticmethod         
     def AVL_UpdateHeight(Data):
        left = -1
        if Data is None:
            left = Data.height
        right = -1
        
        if Data.right is not None:
            right = Data.right.height
        Data.height = max(left,right) + 1
    
     def AVL_Rebalance(self , Data):
        self.AVL_UpdateHeight(Data)
        
        if self.AVL_UpdateHeight(Data) == -2:
           self.AVL_RotateRight(self, Data.right)
           return self.AVL_RotateLeft(self,Data)
    
     def AVL_rotateLeft(self,node):
        Root = node.right
        Temporary = Root.left
        
        Root.left = node
        node.right = Root
        
        node.height = 1 + max (self.getHeight(node.left), self.getHeight(node.right))
        Root.height = 1 + max(self.getHeight(Root.left), self.getHeight(Root.right))
        
        return Root
    
     def AVL_rotateRight(self,node2):
        Root = node2.left
        Temporary = Root.right
        
        Root.right = node2
        node2.left =Temporary
        
        node2.height = 1 + max (self.getHeight(node2.left), self.getHeight(node2.right))
        Root.height = 1 + max(self.getHeight(Root.left), self.getHeight(Root.right))
        
        return Root
    
     def printTree(self,node):
        if node is None:
            return 
        self.printTree(node.left)
        print(node.item)
        self.printTree(node.right)
        
        
class RBtree:
    Root = None
    #count = 0
    height = 0
    def __init__(self,root = None):
         self.root = root
         self.color = "black"
         
    def RBtreeUpdateHeight(Data):
        left = -1
        if Data is not None:
            left = Data.height
        right = -1
        if Data.right is not None:
            right = Data.right.height
        Data.height = max(left,right) + 1  
    
    def RBtreeReplaceChild(parent,C_child, child):
        c = AVL()
        if parent.left is C_child:
            return c.AVLTreeSetChild(parent,"left", child)
        elif(parent.right is C_child):
            return c.AVLTreeSetChild(parent,"right", child)
        return False 
    
    def RBtreeSetChild(self,parent,C_child,child):
        if C_child != "left" and C_child != "right":
            return False
        if C_child == "left":
            parent.left = child
        else:
            parent.right = child
        if child != None:
            child.parent = parent
            
    def RBltreeRotateLeft(self,Data):
        rightLChild = Data.right.left
        if Data.parent is None:
            self.RBtreeReplaceChild(Data.parent,Data,Data.right)
        else:
            self.root = Data
            self.root.parent = None 
        self.RBltreeSetChild(Data.right,"left",Data)
        self.RBtreeSetChild(Data,"right",rightLChild)   
    
    def RBtreeRotateRight(self,Data):
        leftRChild = Data.left.right
        if Data.parent is not None:
            self.RBtreeReplaceChild(Data.parent,Data,Data.right)
        else:
            
            self.root = Data.right
            self.root.parent = None
        self.RBtreeSetChild(Data.left,"right",Data)
        self.RBlacktreeSetChild(Data,"left",leftRChild)
        
    def BalanceRBtree(self,Data):       # rebalancing tree if needed
        if Data.parent is None:
            Data.color = "black"
            return
        if Data.parent.color == "black":
            return
        parent = Data.parent
        grandparent = self.RBGrandParent(Data)
        uncle = self.RBUncle(Data)
        if uncle is not None and uncle.color == "red":
            parent.color = uncle.color = "black"
            self.BalanceRBtree(grandparent)
            return 
        if Data is parent.right and parent is grandparent.left:
            self.RBtreeRotateRight(parent)
            Data = parent
            parent = Data.parent
        elif Data is parent.left and parent is grandparent.right:
            self.RBtreeRotateRight(parent)
            Data = parent
            parent = Data
        parent.color = "black"    
        grandparent.color = "red"
        if Data is parent.left:
            self.RBtreeRotateRight(grandparent)
        else:
            self.RBtreeRotateLeft(grandparent)  
    
    def RBGrandParent(node):
        if node.parent is None:
            return None
        return node.parent.parent
    
    def RBUncle(node):
        grandparent = None
        if node.parent is not None:
            grandparent = node.parent.parent
        if grandparent is None:
            return None
        if grandparent.left is node.parent:
            return grandparent.right
        else:
            return grandparent.left
   
    def insert(self,Data):              # inserting my values into my Tree
        new_item = Node(Data)           # the height also updates
        if self.root is None:
            self.root = new_item
            self.root.color = "black" 
            new_item.height = new_item.height + 1
            return
        new_item.height = new_item.height + 1
        current = self.root
        while current is not None:
            if new_item.item < current.item:
                if current.left is None:
                    current.left = new_item
                    new_item.parent = current
                    current = None
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = new_item
                    new_item.parent = current
                    current = None
                else:
                    current = current.right
        new_item.color = "red"
        
        while new_item is not None: 
            self.BalanceRBtree(new_item)
            new_item = new_item.parent
      
def TreeSearch(word):  #searching for my value inside of the tree
    call = AVL()
    if call.root is None or call.root == word: 
        return True 
    if call.root.item < word:
        return call.TreeSearch(call.root.left,word)
    elif call.root.item > word:
        return call.TreeSearch(call.root.right, word)
    return False
        
def SearchAnagrams(Anagram): # method to look for anagrams insidde of the tree
    call = AVL()
    if call.root is None:
        return False
    if call.root == Anagram:
        return True
    else:
        return TreeSearch(Anagram)
    return False

def print_anagrams(word, prefix=""):
     if len(word) <= 1:
        str = prefix + word
        if TreeSearch(str):
            print(prefix + word)
            return prefix + word
     else:
           for i in range(len(word)):
               cur = word[i: i + 1]
               before = word[0: i] # letters before cur
               after = word[i + 1:] # letters after cur
    
               if cur not in before: # Check if permutations of cur have not been generated.
                  print_anagrams(before + after, prefix + cur)
                 
                    
def RBTreeReadFile(User,file,word): #method to read my file
    call = RBtree()
    line = file.readline()
    while line:
        line =file.readline()
        call.insert(line)
    file.close()
    print_anagrams(word)
                  
def AVLtreeReadFile(UserInput,file,word):     #method to read file 
    call = AVL()                  
    line = file.readline()
    while line:
        line = file.readline() 
        call.insert(line)
    file.close()       
    print_anagrams(word)
                   
def main():
    file = open("words.txt")
    print("please choose which Tree you would like:")
    print("A.AVLTree")
    print("B.RBtree")
    UserInput= input()
    word = input("input a word you would like to search :")
    if UserInput == "AVLTree" or UserInput == "A" or UserInput == "a":
        AVLtreeReadFile(UserInput,file,word)
            
    elif UserInput == "RBtree" or UserInput == "B" or UserInput == "b":
        RBTreeReadFile(UserInput,file,word)
main()                 
                   
                   

    

