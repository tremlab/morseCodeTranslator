# @tremlab
# a python module that builds a populated binary tree for morse code values, with a method to easily translate a morse code string to its letter.

# from morse_code import Morse_Code_Bin_Tree
# mc_tree = Morse_Code_Bin_Tree()
# mc_tree.translate_mc_to_letter("....") => "H"

class Morse_Code_Bin_Tree(object):
    """Class that initializes and populates a binary tree for translating morse code strings into letters.
    """
    def __init__(self):
        self.head = Node("*")

        letters = "ETIANMSURWDKGOHVF*L*PJBXCYZQ**54*3***2**+****16=/*****7***8*90"

        current = self.head
        nexts = []

        for char in letters:
            if current.left == None:
                current.left = Node(char)
            else:
                if current.right == None:
                    current.right = Node(char)
                else:
                    nexts.append(current.left)
                    nexts.append(current.right)
                    current = nexts.pop(0)
                    current.left = Node(char)

    def translate_mc_to_letter(self, mc_ltr_str):
        """method that takes a string input of morse code, traverses the morse code binary tree, and returns the correct letter for that sequnce.
            e.g. "...." => "H"
        """
        current = self.head

        for char in mc_ltr_str:
            if char == ".":
                current = current.left
            else:
                current = current.right

        return current.val


class Node(object):
    """binary node"""
    def __init__(self, char):
        self.val = char
        self.left = None
        self.right = None
