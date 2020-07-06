

class Tree:     
    def __init__(self): 
        self.data = None 
        self.left = None
        self.right = None 

def make_tree(sorted_list): 
    if len(sorted_list) == 1: 
        tree = Tree()
        tree.data = sorted_list[0] 
        return tree 
    middle = int(len(sorted_list)/2) 
    tree = Tree()
    tree.data = sorted_list[middle] 
    tree.left = make_tree(sorted_list[:middle])
    tree.right = make_tree(sorted_list[middle+1:])
    return tree 

sorted_list = [1, 2, 3, 4, 5, 6, 7] 
otree = make_tree(sorted_list) 
print (otree.left.right.data) 
