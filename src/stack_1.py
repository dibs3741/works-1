from typing import List


class cNode:
    indextolist: List[int]

    def __init__(self, size):
        self.onelist = [0 for i in range(size)]
        self.indextolist = [0, int(size/3*1), int(size/3*2)]
        self.depthoflist = [0, 0, 0]
        self.listisempty = [0, 0, 0]
        self.listisfull = [0, 0, 0]

    def put(self, id, val):
        if id < 2:
            if self.indextolist[id] + self.depthoflist[id] == self.indextolist[id+1]:
                print("stack {} is full. cannot put {}.".format(id, val))
                return
        if id >= 2:
            if self.indextolist[id] + self.depthoflist[id] == len(self.onelist):
                print("stack {} is full. cannot put {}.".format(id, val))
                return
        idx = self.indextolist[id] + self.depthoflist[id]
        self.onelist[idx] = val
        self.depthoflist[id] += 1

    def showlist(self):
        print(self.onelist)
        print("size: {}".format(len(self.onelist)))
        print("depth: {}".format(self.depthoflist))


oNode = cNode(21)
oNode.put(1, 33)
oNode.put(1, 34)
oNode.put(1, 35)
oNode.put(1, 36)
oNode.put(1, 37)
oNode.put(1, 38)
oNode.put(1, 39)
oNode.put(1, 44)
oNode.showlist()
oNode.put(2, 13)
oNode.put(2, 14)
oNode.put(2, 15)
oNode.put(2, 16)
oNode.put(2, 17)
oNode.put(2, 18)
oNode.put(2, 19)
oNode.put(2, 24)
oNode.showlist()

print ("hello")

