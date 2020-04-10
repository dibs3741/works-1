
class cNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def print_ll(llst_holder):
    llst_pointer = llst_holder
    while llst_pointer is not None:
        print(llst_pointer.data)
        llst_pointer = llst_pointer.next


lstElements = ['a','b','c','a','a','x']

llst_holder = cNode(lstElements[0])
llst_pointer = llst_holder
for i in lstElements[1:]:
    o = cNode(i)
    llst_pointer.next = o
    llst_pointer = o

visited = []
llst_pointer = llst_holder
llst_pointer_prev = None

while llst_pointer is not None:
    if llst_pointer.data in visited:
        llst_pointer_prev.next = llst_pointer.next
    else:
        visited.append(llst_pointer.data)
        llst_pointer_prev = llst_pointer
    llst_pointer = llst_pointer.next
print_ll(llst_holder)
