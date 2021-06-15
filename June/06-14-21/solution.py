class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def main():
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    try:
        assert deserialize(serialize(node)).left.left.val == 'left.left'
        print("passed test!")
    except AssertionError:
        print("Failed test. Try again.")

def serialize(root):

    if not root:
        return None

    data = []
    queue = []
    queue.append(root)

    while queue:
        node = queue.pop(0)
        if node:
            data.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            data.append("#")
    
    # remove trailing characters
    while data[-1] == "#":
        data.pop()

    print(f"String after serialization: {data}")

    return data

def deserialize(s):

    if not s:
        return None

    root = Node(s[0])
    i = 1
    queue = []
    queue.append(root)
    while queue and i <= (len(s) - 1):
        node = queue.pop(0)
        if s[i] != "#":
            left = Node(s[i])
            node.left = left
            queue.append(left)
        i += 1
        if i > len(s)-1:
            break
        if s[i] != "#":
            right = Node(s[i])
            node.right = right
            queue.append(right)
        i += 1
    return root

if __name__ == "__main__":
    main()