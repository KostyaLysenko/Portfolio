# from binarytree import *


#
# root = Node(3)
# root.left=Node(5)
# root.right = Node(10)
#
# print(root)
# print(list(root))
# print(root.inorder)
# print(root.preorder)
# print(root.size)
# print(root.height)
# print(root.properties)
#
# tree=[8,3,10,1,6,None,14,None,None,4,7,None,None,13,None]
# binary_tree = build(tree)
# print(binary_tree)
# print(binary_tree.properties)

from binarytree import tree

root = tree()
print(root)

root2 = tree(height=2)
print(root2)
root3 = tree(height=2, is_perfect=True)
print(root3)
