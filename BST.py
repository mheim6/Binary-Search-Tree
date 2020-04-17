

class node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None
        self.counter = 0
        self.dupCounter = 0
        self.height = 0


class binary_search_tree:
    def __init__(self):
        self.root = None
        self.counter = 0
        self.dupCounter = 0

    def insert(self, value):
        self.counter = self.counter + 1
        if self.root == None:
            self.root = node(value)
        else:
            self._insert(value, self.root)
            #self.counter = self.counter + 1
        #print("Total Inserted: ", str(self.counter))
        return str(self.counter)


    def _insert(self, value, cur_node):
        if value == cur_node.value:
            self.dupCounter += 1
            #print("This value is already in the tree = ", value)
            self.counter = self.counter - 1

        elif value < cur_node.value:
            if cur_node.left_child == None:
                cur_node.left_child = node(value)
                cur_node.left_child.parent = cur_node
            else:
                self._insert(value, cur_node.left_child)
        else:
            if cur_node.right_child == None:
                cur_node.right_child = node(value)
            else:
                self._insert(value, cur_node.right_child)
                cur_node.right_child.parent = cur_node



    def printCounters(self):
        if self.root is not None:
            self.printCounters_(self.root)

    def printCounters_(self, cur_node):
        print("Inserted = ", cur_node.counter)
        print("Height =", self.height())

    def print_tree(self):
        if self.root != None:
                self._print_tree(self.root)

    def _print_tree(self, cur_node):
        if cur_node != None:
            self._print_tree(cur_node.left_child)
            print(str(cur_node.value))
            self._print_tree(cur_node.right_child)


    def height(self):
        if self.root is not None:
            print("Height of BST tree is : ", self._height(self.root,0))
            return self._height(self.root,0)
        else:
            return 0

    def _height(self, cur_node, cur_height):
        if cur_node == None:
            return cur_height
        left_height = self._height(cur_node.left_child, cur_height + 1)
        right_height = self._height(cur_node.right_child, cur_height + 1)
        return max(left_height, right_height)


    def search(self, value):
        if self.root != None:
            return self._search(value, self.root)
        else:
            return False

    def _search(self, value, cur_node):
        if value == cur_node.value:
            return True
        elif value < cur_node.value and cur_node.left_child != None:
            return self._search(value, cur_node.left_child)
        elif value > cur_node.value and cur_node.right_child != None:
            return self._search(value, cur_node.right_child)
        return False

    def _getDups(self):
        return self.dupCounter


tree = binary_search_tree()




