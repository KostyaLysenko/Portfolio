from Tree import Node
import random

root = Node(5)
root.left=Node(2)
root.right=Node(6)

# print("Прямий обхід дерева:")
# root.travers_pre_order()
#
# print("Зворотній обхід дерева:")
# root.travers_in_order()
# print("*"*50)

a= [5,10,3,49,1, 66]
root.insert_list(a)
root.travers_in_order()
print("***")
root.display()
root.travers_max_order()
root.travers_in_order()
# root.travers_min_order()
# root.delete_key(49)
# root.display()
root.insert(7)
root.display()

