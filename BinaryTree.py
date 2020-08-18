class node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def preorder(node):
    # 데이터 있으면 처리
    if node.data is not None:
        out.append(node.data)
        node.data = None
    # left 있으면 left로 이동
    if node.left is not None:
        preorder(node.left)
    # right 있으면 right로 이동
    if node.right is not None:
        preorder(node.right)

def inorder(node):
    if node.left is not None:
        inorder(node.left)
    if node.data is not None:
        out.append(node.data)
        node.data = None
    if node.right is not None:
        inorder(node.right)

def postorder(node):
    if node.left is not None:
        postorder(node.left)
    if node.right is not None:
        postorder(node.right)
    if node.data is not None:
        out.append(node.data)
        node.data = None


Tree = []
out = []

# 노드 생성
for n in range(16):
    Tree.append(node(n))

# 트리 구조 적용
for n in Tree:
    if n.data % 2 == 0:
        Tree[int(n.data/2)].left = n
    else:
        Tree[int(n.data/2)].right = n

postorder(Tree[1])

print(out)