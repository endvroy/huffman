class BinaryTree:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def setValue(self, value):
        self.value = value

    def setLeft(self, subTree):
        self.left = subTree

    def setRight(self, subTree):
        self.right = subTree

    def insertLeft(self, subTree):
        if self.left is None:
            self.setLeft(subTree)
            return
        else:
            raise Exception

    def insertRight(self, subTree):
        if self.right is None:
            self.setRight(subTree)
            return
        else:
            raise Exception

    def isLeaf(self):
        return self.left is None and self.right is None

    # def preOrder(self, l=None):
    #     if l is None:
    #         l = []
    #     self.left.preOrder(self.left, l)
    #     l.append(self.value)
    #     self.right.preOrder(self.right)
    #     return l
