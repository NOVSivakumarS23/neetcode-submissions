/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:

    TreeNode* invertTree(TreeNode* root) {
        if(root==nullptr){return root;}
        stack<TreeNode*> stacker;
        stacker.push(root);
        while(stacker.empty()==false){
            TreeNode* cur = stacker.top();
            stacker.pop();

            if(cur==nullptr){continue;}
            TreeNode* temp = cur->left;
            cur->left = cur->right;
            cur->right = temp;
            stacker.push(cur->left);
            stacker.push(cur->right);
        }
        return root;
    }
};
