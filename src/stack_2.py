from typing import List


class cNode:
    indextolist: List[int]

    def __init__(self, size):
        self.onelist = []
        self.currmin = []
        self.indextolist = -1
        self.indextomin = -1

    def put(self, val):
        self.indextolist = self.indextolist + 1
        self.onelist.append(val)
        if self.indextomin == -1 or self.currmin[self.indextomin] >= val :
            self.indextomin = self.indextomin+1
            self.currmin.append(val)

    def pop(self):
        v = self.onelist.pop(self.indextolist)
        self.indextolist = self.indextolist - 1

        if self.currmin[self.indextomin] == v:
            m = self.currmin.pop(self.indextomin)
            self.indextomin = self.indextomin-1

    def showlist(self):
        print(self.onelist)
        print(self.currmin[self.indextomin])


oNode = cNode(21)
oNode.put(5)
oNode.showlist()
oNode.put(6)
oNode.showlist()
oNode.put(3)
oNode.showlist()
oNode.put(7)
oNode.showlist()
oNode.pop()
oNode.showlist()
oNode.pop()
oNode.showlist()
