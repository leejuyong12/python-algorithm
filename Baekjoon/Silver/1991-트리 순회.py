N = int(input())
tree = {}

for n in range(N):
    root, left, right = input().split()
    tree[root] = [left, right]

# 전위순회  root -> left -> right 순
def preorder(root):
    if root != '.':
        print(root, end='')     # root
        preorder(tree[root][0]) # left
        preorder(tree[root][1]) # right

# 중위순회  left -> root -> right
def inorder(root):
    if root != '.':
        inorder(tree[root][0])  # left
        print(root, end='')     # root
        inorder(tree[root][1])  # right

# 후위순회  left -> right -> root
def postorder(root):
    if root != '.':
        postorder(tree[root][0]) # root
        postorder(tree[root][1]) # right
        print(root, end='')      # root

preorder('A')
print()
inorder('A')
print()
postorder('A')