# 1305. All Elements in Two Binary Search Trees

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        res = []
        
        def binarySearch(current, vals):
            if current:
                stack = [current]
                while stack:
                    current = stack.pop()
                    vals.append(current.val)
                    if current.right:
                        stack.append(current.right)
                    if current.left:
                        stack.append(current.left)
        
        val_1 = binarySearch(root1, res)
        val_2 = binarySearch(root2, res)
        
        return sorted(res)