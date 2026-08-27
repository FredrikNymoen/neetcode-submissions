# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorderHash = {};
        for i in range(len(inorder)):
            inorderHash[inorder[i]] = i;
        
        preorder.reverse();
        return self.build(preorder, inorderHash, 0, len(inorder) - 1);
    
    def build(self, postorder, inorderHash, start, end):
        if start > end:
            return;
        
        postorderNum = postorder.pop();
        curIdx = inorderHash[postorderNum];
        root = TreeNode(postorderNum);
        
        root.left = self.build(postorder, inorderHash, start, curIdx - 1);
        root.right = self.build(postorder, inorderHash, curIdx + 1, end);
        return root;