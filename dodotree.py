from queue import SimpleQueue
from fractions import Fraction

from bst import BstNode as btnode


class dodotree(btnode):
    def __init__(self, start: Fraction):
        self.treeroot = btnode(start)

        # keeping track of nodes
        self.visited = []
        self.queue = SimpleQueue()

    @staticmethod
    def op0(x):
        if x == 0:
            return 0
        return -1 / x

    @staticmethod
    def op1(x):
        return x + 1

    def create(self, maxelems=5):
        """create tree, breath first

        migth be called multiple times with incread maxelems

        using breath first because the depth is infinite
        maxelems is be +1 of the entered value
        left branch is op0 used, right branch is op1 used
        """
        if len(self.visited) > maxelems:
            raise ValueError("maxelems has been already reached")

        if self.visited == []:
            # if first construction of tree
            bt = self.treeroot
            self.queue.put(bt)
            self.visited.append(bt.key)

        kounter = 0
        while len(self.visited) < maxelems:
            node = self.queue.get()  # this queue shoud never get empty
            # print(f"processing {node}")

            l = self.op0(node.key)
            if l not in self.visited:
                self.visited.append(l)
                node.left = btnode(l)
                self.queue.put(node.left)
                kounter += 1

            r = self.op1(node.key)
            if r not in self.visited:
                self.visited.append(r)
                node.right = btnode(r)
                self.queue.put(node.right)
                kounter += 1

        # I don't keep track of the nodes, (tree is zoomed)
        print(f"added {kounter} nodes, \"unknown\" of which is below tree")

    def search(self, tree):
        """search the tree and return the node if found, else None"""
        pass

    def zoom(self, tree, num):
        """zoom to tree below num"""
        pass

    def print_steps(self, node_key):
        """prints steps to reach `to_node`"""
        # I'm sure this can be done more efficiently
        def _steps(from_node, to_number, mem, curr=0, out=500):
            # this implementation is not complete,
            
            # DOESNT WORK rn
            
            if from_node.key == to_number:
                print(f"reached at target {to_number}")
                # end
                
            if curr > out:
                return
    

            _steps(from_node.left, to_number, mem, curr + 1, out)
            
            _steps(from_node.right, to_number, mem, curr + 1, out)
                
            
            
        mem = []
        _steps(self.treeroot, node_key, mem)

    def display(self):
        self.treeroot.display()


if __name__ == "__main__":
    dt = dodotree(Fraction(1, 1))
    dt.create(maxelems=30)  # this gives 31 elements
    dt.display()
