from binaryTree import BinaryTree
from collections import deque


class HuffmanTree(BinaryTree):
    def __init__(self, value=None, left=None, right=None):
        super().__init__(value=value, left=left, right=right)
        self.leftCode = 0
        self.rightCode = 1

    def getEncoding(self, encoding=None, path=None):
        """extract a encoding dictionary from the huffman tree
        the keys are the symbols, the values are the corresponding encodings
        DO NOT pass in any parameter"""
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


def buildHuffmanTree(freqDict):
    shadowDict={HuffmanTree(key):value for key,value in freqDict.items()}

    while len(shadowDict) > 1:
        leastNode = min(shadowDict, key=shadowDict.get)
        leastFreq = shadowDict.pop(leastNode)

        secondNode = min(shadowDict, key=shadowDict.get)
        secondFreq = shadowDict.pop(secondNode)

        tree = HuffmanTree(left=leastNode, right=secondNode)
        shadowDict[tree] = leastFreq + secondFreq

    return list(shadowDict.keys())[0]


def huffmanEncode(encoding, pattern):
    code = ''
    for symbol in pattern:
        code += ''.join([str(x) for x in list(encoding[symbol])])
    return code


def huffmanDecode(tree, code):
    pattern = ''
    node = tree
    for digit in code:
        if int(digit) == 0:
            node = node.left
        else:
            node = node.right
        if node.isLeaf():
            pattern += node.value
            node = tree
    return pattern


if __name__ == '__main__':
    freqDict = {'A': 1 / 3,
                'B': 1 / 2,
                'C': 1 / 12,
                'D': 1 / 12}
    tree = buildHuffmanTree(freqDict)
    print(tree.getEncoding())
    code = huffmanEncode(tree.getEncoding(), 'ABCD')
    print(code)
    print(huffmanDecode(tree, code))

    freqDict = {'A': 0.11,
                'E': 0.25,
                'I': 0.20,
                'O': 0.35,
                'U': 0.09}
    tree = buildHuffmanTree(freqDict)
    print(tree.getEncoding())
    code = huffmanEncode(tree.getEncoding(), 'AEIOU')
    print(code)
    print(huffmanDecode(tree, code))
