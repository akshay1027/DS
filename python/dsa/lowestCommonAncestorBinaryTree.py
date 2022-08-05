# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root

        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right

            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left

            else:
                return cur


# c++ solution

# /**
#  * Definition for a binary tree node.
#  * struct TreeNode {
#  *     int val;
#  *     TreeNode *left;
#  *     TreeNode *right;
#  *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
#  * };
#  */

# class Solution {
# public:
#     TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
#         TreeNode* cur = root;

#         while(true) {
#             if (p->val > cur->val && q->val > cur->val)
#                 cur = cur->right;

#             else if (p->val < cur->val && q->val < cur->val)
#                 cur = cur->left;

#             else
#                 return cur;
#         }
#     }
# };
