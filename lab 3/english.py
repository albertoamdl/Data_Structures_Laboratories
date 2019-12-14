from AVLTree import AVLTree, Node

import operator

from redbt import RedBlackTree


class AVL:

    def __init__(self, word, tree):

        self.word = word

        self.tree = tree

    # This method is used to read in the file and throw in onto the tree.

    def read_file(self):

        # In this instance self.words is actually the list of everyword in test_words.txt

        top10 = {}

        for word in self.word:

            x = 0

            if self.tree.search(word.lower()):

                x += 1

                # This will count the words that have already appeared.
                for i in range(len(word)):

                    cur = word[i: i+1]

                    before = word[0:i]

                    after = word[i+1:]

                    anagram = "{}{}{}".format(after, before, cur)

                    if self.tree.search(anagram.lower()) and anagram.lower() != word.lower():

                        x += 1

            top10[word] = x

        sorted_top10 = sorted(top10.items(), key=operator.itemgetter(1))

        forcheck = 0

        for top in reversed(sorted_top10):

            forcheck += 1

            if forcheck == 11:

                break

            if top[1] == 1:

                print("{}. \"{}\" has {} anagram".format(
                    forcheck, top[0], top[1]))

            else:

                print("{}. \"{}\" has {} anagrams".format(
                    forcheck, top[0], top[1]))

    def main(self):

        word = self.tree.search(self.word.lower())

        count = 0

        anagram_count = 0

        anagram_list = []

        if word:

            for i in range(len(self.word)):

                cur = self.word[i: i+1]

                before = self.word[0:i]

                after = self.word[i+1:]

                # Displays the anagrams that were found.
                anagram = "{}{}{}".format(after, before, cur)

                count += 1

                # Adds the word to the list of anagrams.
                if anagram.lower() != self.word.lower():

                    anagram_list.append(anagram)

                # Displays the anagram that was found.
                if self.tree.search(anagram.lower()) and anagram.lower() != self.word.lower():

                    print("Anagram found: {}".format(anagram))

                    anagram_count += 1

            print("\nI went through {} possible anagrams".format(count))

            if anagram_count == 1:

                print("I found {} anagram".format(anagram_count))

            else:

                print("I found {} anagrams".format(anagram_count))

            print("I tried these anagrams:\n{}".format(anagram_list))

        else:

            print("The word was not found :(")


class RedBlack:

    def __init__(self, word, tree):  # Initializes the RedBlack tree

        self.word = word

        self.tree = tree

    def read_file(self):

        # In this instance self.words is actually the list of everyword in test_words.txt

        top10 = {}

        for word in self.word:

            x = 0

            if self.tree.search(word.lower()):

                x += 1

                for i in range(len(word)):

                    cur = word[i: i+1]

                    before = word[0:i]

                    after = word[i+1:]

                    anagram = "{}{}{}".format(after, before, cur)

                    if self.tree.search(anagram.lower()) and anagram.lower() != word.lower():

                        x += 1

                top10[word] = x

        sorted_top10 = sorted(top10.items(), key=operator.itemgetter(1))

        forcheck = 0

        # This is used to sort out the top 10 list

        for top in reversed(sorted_top10):

            forcheck += 1

            if forcheck == 11:

                break

            if top[1] == 1:

                print("{}. \"{}\" has {} anagram".format(
                    forcheck, top[0], top[1]))

            else:

                print("{}. \"{}\" has {} anagrams".format(
                    forcheck, top[0], top[1]))

    def main(self):

        word = self.tree.search(self.word.lower())

        count = 0

        anagram_count = 0

        anagram_list = []

        if word:

            for i in range(len(self.word)):

                cur = self.word[i: i+1]

                before = self.word[0:i]

                after = self.word[i+1:]

                anagram = "{}{}{}".format(after, before, cur)

                count += 1

                if anagram.lower() != self.word.lower():

                    anagram_list.append(anagram)

                if self.tree.search(anagram.lower()) and anagram.lower() != self.word.lower():

                    print("Anagram found: {}".format(anagram))

                    anagram_count += 1

            print("\nI went through {} possible anagrams".format(count))

            if anagram_count == 1:

                print("I found {} anagram".format(anagram_count))

            else:

                print("I found {} anagrams".format(anagram_count))

            print("I tried these anagrams:\n{}".format(anagram_list))

        else:

            print("The word was not found :(")


with open("words.txt", "r") as txt:

    print("Just press enter when giving a word if you want to exit.")

    # Prompts user for which tree they would like to use.
    choice = input("Do you want to use the AVL or redblacktree algorithm?\n")

    # Everything here will be for the redblack tree

    if choice.lower() == "redblacktree":

        choice = input(

            "Do you want to input words yourself or do you want to use test_words.txt?\nEnter either: myinput or test_words\n")

        # Everything here will load the tree with the text file.

        if choice.lower() == "test_words":

            with open("test_words.txt", "r") as subtxt:

                print("\nLoading up the RedBlackTree...\n")

                tree = RedBlackTree()

                sublines = subtxt.readlines()

                sublines = list(map(lambda s: s.strip(), sublines))

                lines = txt.readlines()

                lines = list(map(lambda s: s.strip(), lines))

                for key in lines:

                    tree.insert(key.lower())

                print("Tree loaded!")

                print('Red-black tree with ' + str(len(tree)) +
                      ' nodes has height of ' + str(tree.get_height()))

                Engine = RedBlack(sublines, tree)

                Engine.read_file()

        # Everything here will load the tree with the word of choice.

        else:

            print("Loading up the RedBlackTree....")

            tree = RedBlackTree()

            lines = txt.readlines()

            lines = list(map(lambda s: s.strip(), lines))

            for key in lines:

                tree.insert(key.lower())

            print("Tree loaded!")

            print('Red-black tree with ' + str(len(tree)) +
                  ' nodes has height of ' + str(tree.get_height()))

            quit = True

            while quit:

                word = input("\nGive me a word:\n")

                if word == "":

                    quit = False

                else:

                    Engine = RedBlack(word, tree)

                    Engine.main()

    # -------------------

    # This is the AVL Tree part

    if choice.lower() == "avl":

        choice = input(

            "Do you want to input words yourself or do you want to use test_words.txt?\nEnter either: myinput or test_words\n")

        if choice.lower() == "test_words":

            with open("test_words.txt", "r") as subtxt:

                print("\nLoading up the AVL Tree...\n")

                tree = AVLTree()

                sublines = subtxt.readlines()

                sublines = list(map(lambda s: s.strip(), sublines))

                lines = txt.readlines()

                lines = list(map(lambda s: s.strip(), lines))

                for key in lines:

                    node = Node(key.lower())

                    tree.insert(node)

                print("Tree loaded!")

                Engine = AVL(sublines, tree)

                Engine.read_file()

        else:

            print("\nLoading up the AVL Tree...\n")

            tree = AVLTree()

            quit = True

            lines = txt.readlines()

            lines = list(map(lambda s: s.strip(), lines))

            for key in lines:

                node = Node(key.lower())

                tree.insert(node)

            print("Tree loaded!")

            while quit:

                word = input("\nGive me a word:\n")

                if word == "":

                    quit = False

                else:

                    Engine = AVL(word.strip(), tree)

                    Engine.main()
