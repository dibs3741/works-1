
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


def find_dupe_without_buffer(llst_holder):
    llst_pointer = llst_holder
    llst_pointer_runner = llst_holder.next
    llst_pointer_prev = llst_holder

    while llst_pointer is not None:
        while llst_pointer_runner is not None:
            if llst_pointer.data == llst_pointer_runner.data:
                llst_pointer_prev.next = llst_pointer_runner.next
                llst_pointer_runner = llst_pointer_runner.next
                continue
            llst_pointer_prev = llst_pointer_prev.next
            llst_pointer_runner = llst_pointer_runner.next
        llst_pointer = llst_pointer.next
        llst_pointer_prev = llst_pointer


lstElements = ['a','b','c','a','a','x']
llst_holder = create_linklist_from_list(lstElements)
find_dupe_without_buffer(llst_holder)
print_ll(llst_holder)

