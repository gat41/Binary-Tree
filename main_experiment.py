
import sys
import os
from Binary_Tree_Functions import BinaryTree, create_tree, print_tree, create_numbers

path = os.path.abspath(os.path.dirname(__file__))
type = sys.getfilesystemencoding()
filename = 'output.txt'
original_stdout = sys.stdout # Save a reference to the original standard output

list_of_numbers = create_numbers()           # Create 100 random numbers and store it in "list_of_numbers".
my_tree = BinaryTree(list_of_numbers, 'X')   # Initialize "list_of_numbers": equip it with "LeftChild" and "RightChild".
my_tree = create_tree(my_tree)               # Call function "create_tree" to create the tree.

file = open(filename, 'w')
sys.stdout = file # Change the standard output to the file we created.
print('node\t\tmin\t\tmax\t\tnum_of_points')  # Print the title.
print_tree(my_tree)                           # Call function "print_tree" to print out the required information.
file.close() # without this line, I was not able to see the output in the text file
    
sys.stdout = original_stdout # Reset the standard output to its original value

