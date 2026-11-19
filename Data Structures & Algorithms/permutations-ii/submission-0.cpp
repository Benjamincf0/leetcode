class Solution {
public:
    void dfs(vector<vector<int>>& res, vector<int>& nums, int i) {
        if (i == nums.size()) {
            vector<int> yes = nums;
            res.push_back(yes);
        }

        std::unordered_set<int> used;

        for (int j = i; j < nums.size(); j++) {
            if (used.count(nums[j])) continue; // means we already tried nums[j] at this position.
            used.insert(nums[j]);

            int temp = nums[j]; // old j
            nums[j] = nums[i]; // old i
            nums[i] = temp;
            dfs(res, nums, i+1);
            nums[i] = nums[j];
            nums[j] = temp;
        }
    }

    vector<vector<int>> permuteUnique(vector<int>& nums) {
        vector<vector<int>> res = {};
        dfs(res, nums, 0);
        return res;
    }
};

// 1 1 2
//   i
//   j
// res [ 112 121 112 121 ]