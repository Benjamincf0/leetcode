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
    TreeNode* dfs(vector<int>& preorder, std::unordered_map<int,int>& ino_map, int pre_l, int pre_r, int ino_l) {
        if (pre_l == pre_r) return nullptr;

        TreeNode* root = new TreeNode(preorder[pre_l]);
        int sep = ino_map[preorder[pre_l]]-ino_l;

        root->left = dfs(preorder, ino_map, pre_l+1, pre_l+sep+1, ino_l);
        root->right = dfs(preorder, ino_map, pre_l+sep+1, pre_r, ino_l+sep+1);

        return root;
    }

    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        std::unordered_map<int,int> ino_map;
        for (int i = 0; i < inorder.size(); i++) {
            ino_map.insert({inorder[i], i});
        }
        return dfs(preorder, ino_map, 0, preorder.size(), 0);
    }
};