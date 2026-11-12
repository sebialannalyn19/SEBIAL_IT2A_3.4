
from collections import deque

def binary_tree():

    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    root = Node("S")
    root.left = Node("E")
    root.right = Node("B")
    root.left.left = Node("I")
    root.left.right = Node("A")
    root.right.right = Node("L")

    # BFS
    queue = deque([root])
    bfs_result = []

    while queue:
        node = queue.popleft()
        bfs_result.append(node.data)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    # DFS - Preorder
    def dfs(node):
        if node is None:
            return []

        return ([node.data]
                + dfs(node.left)
                + dfs(node.right))

    print("BFS:", bfs_result)
    print("DFS:", dfs(root))
