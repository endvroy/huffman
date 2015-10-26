from binaryTree import BinaryTree
from collections import deque


class HuffmanTree(BinaryTree):
    def __init__(self, value=None, leftNode=None, rightNode=None):
        super().__init__(value=value, leftNode=leftNode, rightNode=rightNode)
        self.leftCode = 0
        self.rightCode = 1

    def getEncoding(self, encoding=None, path=None):
        if encoding is None:
            encoding = {}

        if path is None:
            path = deque()

        if self.isLeaf():
            encoding[self.value] = path.copy()
        else:
            path.append(self.leftCode)
            self.left.getEncoding(encoding, path)
            path.pop()

            path.append(self.rightCode)
            self.right.getEncoding(encoding, path)
            path.pop()

        return encoding


def huffmanEncoding(freqDict):
    keys = list(freqDict.keys())
    for key in keys:
        freqDict[HuffmanTree(value=key)] = freqDict.pop(key)

    while len(freqDict) > 1:
        leastNode = min(freqDict, key=freqDict.get)
        leastFreq = freqDict.pop(leastNode)

        secondNode = min(freqDict, key=freqDict.get)
        secondFreq = freqDict.pop(secondNode)

        tree = HuffmanTree(leftNode=leastNode, rightNode=secondNode)
        freqDict[tree] = leastFreq + secondFreq

    return list(freqDict.keys())[0].getEncoding()


if __name__ == '__main__':
    freqDict = {'A': 1 / 3,
                'B': 1 / 2,
                'C': 1 / 12,
                'D': 1 / 12}
    encoding = huffmanEncoding(freqDict)
    print(encoding)

    freqDict = {'A': 0.11,
                'E': 0.25,
                'I': 0.20,
                'O': 0.35,
                'U': 0.09}
    encoding = huffmanEncoding(freqDict)
    print(encoding)
