class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        // Two pointers O(n) time & O(n) Space
        if (k == 0) return false;
        std::unordered_set<int> set_win;

        for (int i = 0; i < nums.size(); i++) {

            // Think abt it:
            // We have to keep k numbers in our window, so we remove the k+1th.
            if (i >= k+1) {
                set_win.erase(nums[i-(k+1)]);
            }

            // here insert returns a std::pair where the second item
            // is a boolean saying whether it was already present.
            if (!set_win.insert(nums[i]).second) return true;
        }

        return false;
    }
};