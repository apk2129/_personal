# Definition for a binary tree node.
from collections import defaultdict

class TreeNode:

    def __init__(self, v, l=None, r=None):
        self.val = v
        self.left = l
        self.right = r

    '''
    ----------------------------------------------------------------
        V A L I D A T I O N
    ----------------------------------------------------------------
    '''
    def binary_Tree_Paths(self, root):
        if not root: return []

        res, stack = [], [(root, "")]

        while stack:
            node, ls = stack.pop()
            if not node.left and not node.right:
                res.append(ls+str(node.val))
            if node.right:
                stack.append((node.right, ls+str(node.val)+"->"))
            if node.left:
                stack.append((node.left, ls+str(node.val)+"->"))
        return res
    def is_Valid_Binary_Tree(self, root):pass

    '''
    ----------------------------------------------------------------
        T R A V E R S A L S
    ----------------------------------------------------------------
    '''

    def InorderTraversal(self, root):
        # L NODE R
        # Go to LEFTMOST node , keep appending to stack
        # pop -> append  -> move right

        res   = []
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack: return res # <---- return value
            node = stack.pop()
            res.append(node.val)
            root = node.right
    def InorderTraversalR(self, root):

        def recurse(root,res):
            if root:
                recurse(root.left, res)
                res.append(root.val)
                recurse(root.right, res)
        res = []
        recurse(root, res)
        return res

    def PreorderTraversal(self, root):

        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)

        return res
    def PreorderTraversalR(self, root):

        def recurse(root, res):
            if root:
                res.append(root.val)
                recurse(root.left, res)
                recurse(root.right, res)

        res = []
        recurse(root,res)
        return res

    def PostorderTraversal(self, root):
        '''
        1. Create an empty stack, Push root node to the stack.
        2. Do following while stack is not empty.
             2.1. pop an item from the stack and print it.
             2.2. push the left child of popped item to stack.
             2.3. push the right child of popped item to stack.
        3. Reverse the ouput.
        '''
        res = []
        stack = [root]
        while stack:
            print("Stack",[i.val for i in stack if i])
            print("res",res)
            print("====================")
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.left)
                stack.append(node.right)

        return res
    def PostorderTraversalR(self, type):

        def recurse(root,res):
            if root:
                recurse(root.left, res)
                recurse(root.right, res)
                res.append(root.val)
        res = []
        recurse(root, res)
        return res

    def Binary_Tree_Vertical_Order_Traversal(self, root):
        '''
            * Column wise traversal
                   3
                  / \
                 9   8
                /\   /\
               /  \ /  \
              4    01   7

            --> [[4],[9],[3,0,1],[8],[7]]
            * BFS, put node, col into queue at the same time
            * Every left child access col - 1 while right child col + 1
            * This maps node into different col buckets
            * Get col boundary min and max on the fly
            * Retrieve result from cols
        '''
        result = defaultdict(list)
        queue = [(root,0)]
        for node, i in queue:
            if node:
                result[i].append(node.val)
                queue.append((node.left,  i-1))
                queue.append((node.right, i+1))

        return [result[i] for i in sorted(result)]

    def Binary_Tree_Horizontal_Order_Traversal(self, root):

        res = defaultdict(list)
        i = 0
        while root:
            res[i] = root.val
            root = 




    def Binary_Search_Tree_Iterator(self, root): pass


    '''
    ----------------------------------------------------------------
        S E R I A L I Z E / D E - S E R I A L I Z E
    ----------------------------------------------------------------
    '''
    def Serialize_Binary_Tree(self, root):
        def doit(node):
            if node:
                # print(node.val)
                vals.append(str(node.val))
                # print(vals)
                doit(node.left)
                doit(node.right)
            else:
                vals.append('#')
        vals = []
        doit(root)
        return ' '.join(vals)
    def Deserialize_Binary_Tree(self, data):

        for i in data.split():
            if i != '#':
                TreeNode(i)



if __name__=="__main__":
    '''
            1
           / \
          2   5
         / \
        4   3
    '''
    T  = TreeNode( 1,
                   TreeNode(2, TreeNode(4), TreeNode(3)),
                   TreeNode(5, None,None )
         )

    # print(T.binary_Tree_Paths(T))
    # print(T.Serialize_Binary_Tree(T))
    # print(T.Serialize_Binary_Tree(T))
    # print(T.PreorderTraversalR(T))
    # print(T.Binary_Tree_Vertical_Order_Traversal(T))
