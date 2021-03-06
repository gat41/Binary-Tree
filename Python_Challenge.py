import sys
import os
from Binary_Tree_Functions import Logger, BinaryTree, create_tree, print_tree, create_numbers

path = os.path.abspath(os.path.dirname(__file__))
type = sys.getfilesystemencoding()
sys.stdout = Logger('Python_Challenge_Output.txt')     # Store the output into "Python_Challenge_Output.txt" file.


list_of_numbers = create_numbers()           # Create 100 random numbers and store it in "list_of_numbers".
my_tree = BinaryTree(list_of_numbers, 'X')   # Initialize "list_of_numbers": equip it with "LeftChild" and "RightChild".
my_tree = create_tree(my_tree)               # Call function "create_tree" to create the tree.

print('node\t\tmin\t\tmax\t\tnum_of_points')  # Print the title.
print_tree(my_tree)                           # Call function "print_tree" to print out the required information.

# Note that when print out "my_tree", I place a blank line when one level is end.
# This can help us to identify different levels.
# If you don't like this blank line, you can also delete it by deleting the line 58 in "Binary_tree_function.py" file.
