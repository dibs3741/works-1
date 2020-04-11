
class cNode:
    def __init__(self, data):
        self.data = data
        self.next = None


def print_ll(llst_holder1):
    ll = llst_holder1
    while ll is not None:
        print(ll.data)
        ll = ll.next


def create_linklist_from_list(lst):
    llst_holder = cNode(lst[0])
    llst_pointer = llst_holder
    for i in lst[1:]:
        o = cNode(i)
        llst_pointer.next = o
        llst_pointer = o
    return llst_holder


def find_elem_at_pos(linklist, pos):
    if linklist is None:
        return 0, None
    i, val = find_elem_at_pos(linklist.next, pos)
    if i == pos:
        return i+1, linklist.data
    return i+1, val

lstElements = ['a','b','c','a','a','x']
llst_holder = create_linklist_from_list(lstElements)
i, val = find_elem_at_pos(llst_holder, 4)
print (val)

