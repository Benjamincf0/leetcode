class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        if (k == 0) return false;
        std::unordered_set<int> set_win;

        for (int i = 0; i < nums.size(); i++) {
            if (i >= k+1) {
                set_win.erase(nums[i-k-1]);
                // std::cout << "removed " << nums[i-k-1] << '\n';
            }

            if (set_win.contains(nums[i])) return true;
            set_win.insert(nums[i]);

            // std::cout << i << " : ";
            // for (int num : set_win) {
            //     std::cout << num << " ";
            // }
            // std::cout << '\n';
        }

        return false;
    }
};