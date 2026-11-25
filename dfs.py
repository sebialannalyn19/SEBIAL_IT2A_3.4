class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Pre-order: Root -> Left -> Right
def pre_order(node, result):
    if node is None:
        return
    result.append(node.value)
    pre_order(node.left, result)
    pre_order(node.right, result)


# In-order: Left -> Root -> Right
def in_order(node, result):
    if node is None:
        return
    in_order(node.left, result)
    result.append(node.value)
    in_order(node.right, result)


# Post-order: Left -> Right -> Root
def post_order(node, result):
    if node is None:
        return
    post_order(node.left, result)
    post_order(node.right, result)
    result.append(node.value)


def build_assessment_35_tree():
    root = Node("A")

    root.left = Node("N")
    root.right = Node("N")

    root.left.left = Node("A")
    root.left.right = Node("L")
    root.right.left = Node("Y")
    root.right.right = Node("N")

    root.left.left.left = Node("S")
    root.left.left.right = Node("E")

    root.left.right.left = Node("B")
    root.left.right.right = Node("I")

    root.right.left.left = Node("A")
    root.right.left.right = Node("L")

    return root


if __name__ == "__main__":
    root = build_assessment_35_tree()

    pre_result = []
    in_result = []
    post_result = []

    pre_order(root, pre_result)
    in_order(root, in_result)
    post_order(root, post_result)

    print("Pre-order  (Root - Left - Right):", " - ".join(pre_result))
    print("In-order   (Left - Root - Right):", " - ".join(in_result))
    print("Post-order (Left - Right - Root):", " - ".join(post_result))