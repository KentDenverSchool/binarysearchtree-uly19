import unittest

class Node:
    def __init__(self, keyIn, valueIn):
        self.key = keyIn
        self.value = valueIn
        self.left = None
        self.right = None

    def __repr__(self):
        return "Node{ key : " + str(self.key) + ", value : " + str(self.value) + "}"

    def getKey(self):
        return self.key
    def setKey(self, keyIn):
        self.key = keyIn
    def getValue(self):
        return self.value
    def setValue(self, valueIn):
        self.value = valueIn

    def getLeft(self):
        return self.left
    def setLeft(self, nodeIn):
        self.left = nodeIn
    def getRight(self):
        return self.right
    def setRight(self, nodeIn):
        self.right = nodeIn

class BinarySearchTree:
    def __init__(self):
        self.root = Node(None, None)

    def size(self):
        return self.__size(self.root)

    def __size(self, nodeIn):
        if nodeIn == None or nodeIn.getKey() == None:
            return 0
        left = nodeIn.getLeft() == None
        right = nodeIn.getRight() == None
        if left & right:
            return 1
        elif right:
            return 1 + self.__size(nodeIn.getLeft())
        elif left:
            return 1 + self.__size(nodeIn.getRight())
        else:
            return 1 + self.__size(nodeIn.getRight()) + self.__size(nodeIn.getLeft())

    def isEmpty(self):
        return self.size() == 0

    def put(self, keyIn, valueIn):
        if self.root.getKey() == None:
            self.root = Node(keyIn, valueIn)
        else:
            self.root = self.__put(self.root, keyIn, valueIn)

    def __put(self, nodeIn, keyIn, valueIn):
        if nodeIn == None or nodeIn.getKey() == None:
            return Node(keyIn, valueIn)
        else:
            if keyIn > nodeIn.getKey():
                nodeIn.setRight(self.__put(nodeIn.getRight(), keyIn, valueIn))
            else:
                nodeIn.setLeft(self.__put(nodeIn.getLeft(), keyIn, valueIn))
            return nodeIn

    def get(self, keyIn):
        return self.__get(self.root, keyIn)

    def __get(self, curNode, keyIn):
        if curNode == None:
            return None
        if curNode.getKey() == keyIn:
            return curNode.getValue()
        elif curNode.getKey() < keyIn:
            if curNode.getRight() == None:
                return None
            return self.__get(curNode.getRight(), keyIn)
        elif curNode.getKey() > keyIn:
            if curNode.getLeft() == None:
                return None
            return self.__get(curNode.getLeft(), keyIn)

    def contains(self, keyIn):
        return self.get(keyIn) != None

    def remove(self, keyIn):
        value = self.get(keyIn)
        self.root = self.__remove(self.root, keyIn)
        return value

    def __remove(self, nodeIn, keyIn):
        if nodeIn == None:
            return None
        if keyIn < nodeIn.getKey():
            nodeIn.setLeft(self.__remove(nodeIn.getLeft(), keyIn))
        elif keyIn > nodeIn.getKey():
            nodeIn.setRight(self.__remove(nodeIn.getRight(), keyIn))
        else:
            if nodeIn.getRight() == None:
                return nodeIn.getLeft();
            if nodeIn.getLeft() == None:
                return nodeIn.getRight()
            min = self.__min(nodeIn.getRight())
            min.setLeft(nodeIn.getLeft())
            nodeIn = nodeIn.getRight()
        return nodeIn

    def min(self):
        return self.__min(self.root).getKey();

    def __min(self, nodeIn):
        if nodeIn.getLeft() == None:
            return nodeIn
        else:
            return self.__min(nodeIn.getLeft())

    def max(self):
        return self.__max(self.root).getKey();

    def __max(self, nodeIn):
        if nodeIn.getRight() == None:
            return nodeIn
        else:
            return self.__max(nodeIn.getRight())

    def __repr__(self):
        temp = self.toString(self.root)
        temp = temp[0:len(temp)-2]
        return "{" + temp + "}"


    def toString(self, nodeIn):
        if(nodeIn==None):
            return ""
        return self.toString(nodeIn.getLeft()) + str(nodeIn.getKey()) + "=" + str(nodeIn.getValue())  + ", " + self.toString(nodeIn.getRight())


class TestBST(unittest.TestCase):
    def test_put(self):
        bst = BinarySearchTree()
        bst.put(1, "a")
        bst.put(2, "b")
        self.assertEqual(str(bst), '{1=a, 2=b}')

    def test_get(self):
        bst = BinarySearchTree()
        bst.put(1, "a")
        bst.put(2, "b")
        self.assertEqual(str(bst.get(2)), 'b')

    def test_size(self):
        bst = BinarySearchTree()
        self.assertEqual(bst.size(), 0)
        bst.put(1, "a")
        bst.put(2, "b")
        self.assertEqual(bst.size(), 2)

    def test_is_empty(self):
        bst = BinarySearchTree()
        self.assertTrue(bst.isEmpty())
        bst.put(1, "a")
        bst.put(2, "b")
        self.assertFalse(bst.isEmpty())

    def test_min_max(self):
        bst = BinarySearchTree()
        bst.put(1, "a")
        bst.put(2, "b")
        bst.put(0, "c")
        self.assertEqual(bst.min(), 0)
        self.assertEqual(bst.max(), 2)

    def test_contains(self):
        bst = BinarySearchTree()
        bst.put(1, "a")
        bst.put(2, "b")
        bst.put(0, "c")
        self.assertTrue(bst.contains(0))
        self.assertFalse(bst.contains(-9))

    def test_remove(self):
        bst = BinarySearchTree()
        bst.put(1, "a")
        bst.put(2, "b")
        bst.put(0, "c")
        bst.put(-1, "d")
        self.assertEqual(bst.remove(1), 'a')
        self.assertEqual(bst.remove(0), 'c')
        self.assertEqual(bst.remove(-1), 'd')
        self.assertEqual(str(bst), '{2=b}')

if __name__ == '__main__':
    unittest.main()
