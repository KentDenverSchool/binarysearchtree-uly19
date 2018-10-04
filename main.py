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
        self.node = nodeIn
    def getRight(self):
        return self.right
    def setRight(self, nodeIn):
        self.node = nodeIn

class BinarySearchTree:
    def __init__(self):
        self.root = Node(None, None)

    def size(self):
        return self.__size(self.root)

    def __size(self, nodeIn):
        if nodeIn.getLeft() == None & nodeIn.getRight() == None:
            return 1
        elif nodeIn.getLeft() != None & nodeIn.getRight() == None:
            return 1 + self.__put(nodeIn.getLeft())
        elif nodeIn.getLeft() == None & nodeIn.getRight() != None:
            return 1 + self.__put(nodeIn.getRight())
        else:
            return 1 + self.__put(nodeIn.getRight()) + self.__put(nodeIn.getLeft())

    def isEmpty(self):
        return self.size() == 0

    def put(self, keyIn, valueIn):
        if self.root.getKey() == None:
            print(5, self.root)
            self.root = Node(keyIn, valueIn)
        else:
            self.root = self.__put(self.root, keyIn, valueIn)
            print(6, self.root)


    def __put(self, nodeIn, keyIn, valueIn):
        print(1, self.root)
        if nodeIn == None:
            print(2, self.root)
            nodeIn = Node(keyIn, valueIn)
        else:
            if nodeIn.getKey < keyIn:
                if nodeIn.getRight() == None:
                    nodeIn.setRight(Node(keyIn, valueIn))
                else:
                    self.__put(nodeIn.getRight(), keyIn, valueIn)
            if nodeIn.getKey > keyIn:
                if nodeIn.getLeft() == None:
                    nodeIn.setLeft(Node(keyIn, valueIn))
                else:
                    self.__put(nodeIn.getLeft(), keyIn, valueIn)

bts = BinarySearchTree()
bts.put(1, "a")
bts.put(2, "b")
#print(bts.size())
'''
    //recursive put
    //sets left/right or creates a new node appropriately, returns the
    //modified node n
    private Node<Key,Value> put(Node<Key, Value> n, Key key, Value val) {

    }

    //recursive get wrapper
    public Value get(Key key) {
        return get(root, key);
    }

    //recursive get
    //returns null if the key does not exist
    private Value get(Node<Key, Value> n, Key key) {
    }

    public boolean contains(Key key) {
    }

    public Value remove(Key key) {
        Value v = get(key);
        root = remove(root, key);
        return v;
    }

    private Node remove(Node<Key, Value> n, Key key) {
        if(n == null) return null;
        int i = key.compareTo(n.getKey());
        if( i < 0) {
            n.setLeft(remove(n.getLeft(), key));
        } else if(i > 0) {
            n.setRight(remove(n.getRight(), key));
        }else {
            if(n.getRight() == null) return n.getLeft();
            if(n.getLeft() == null) return n.getRight();
            Node min = min(n.getRight());
            min.setLeft(n.getLeft());
            n = n.getRight();
        }
        n.setSize(size(n.getRight()) + size(n.getLeft()) + 1);
        return n;
    }

    public Key min() {
        return min(root).getKey();
    }

    //returns the node at the left most left branch of n
    private Node<Key, Value> min(Node<Key, Value> n) {
    }

    public Key max() {
        return max(root).getKey();
    }

    //returns the node at the right most right branch of n
    private Node<Key, Value> max(Node<Key, Value> n) {

    }

    public String toString() {
        String temp = toString(root);
        temp = temp.substring(0, temp.length()-2);
        return "{" + temp + "}";
    }

    private String toString(Node<Key, Value> n) {
        if(n == null) return "";
        return toString(n.getLeft()) +
                n.getKey() + "=" + n.getValue()  + ", " +
                toString(n.getRight());

    }
'''
