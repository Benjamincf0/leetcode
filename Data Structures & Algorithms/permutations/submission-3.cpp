class Solution {
public:
    void dfs(vector<vector<int>>& res, vector<int>& nums, int i) {
        if (i == nums.size()) {
            vector<int> yes = nums;
            res.push_back(yes);
        }

        for (int j = i; j < nums.size(); j++) {
            int temp = nums[j]; // old j
            nums[j] = nums[i]; // old i
            nums[i] = temp;
            dfs(res, nums, i+1);
            nums[i] = nums[j];
            nums[j] = temp;
        }
    }
    vector<vector<int>> permute(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> res = {};
        dfs(res, nums, 0);
        return res;
    }
};