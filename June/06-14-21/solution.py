class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def main():
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    try:
        assert deserialize(serialize(node)).left.left.val == 'left.left'
        Print("Passed test!")
    except AssertionError:
        print("Failed test. Try again.")

def serialize(root):

def deserialize(s):

if __name__ == "__main__":
    main()