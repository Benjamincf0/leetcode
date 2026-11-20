class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        std::unordered_set<int> targets;

        std::set<std::array<int, 4>> res;

        for (int i = 0; i < nums.size(); i++) {
            int a = nums[i];
            for (int j = i+1; j < nums.size(); j++) {
                int b = nums[j];
                targets.clear();
                for (int k = j+1; k < nums.size(); k++) {
                    int c = nums[k];

                    if ((a > 0 && target < INT_MIN + a) ||
                        (a < 0 && target > INT_MAX + a) ||
                        (b > 0 && target - a < INT_MIN + b) ||
                        (b < 0 && target - a > INT_MAX + b) ||
                        (c > 0 && target - a - b < INT_MIN + c) ||
                        (c < 0 && target - a - b > INT_MAX + c)) {
                            continue;
                    }

                    int d = target-a-b-c;

                    if (targets.contains(d)) {
                        std::array<int,4> soln = {a,b,c,d};
                        std::sort(std::begin(soln),std::end(soln));
                        res.insert(soln);
                    }
                    targets.insert(c);
                }
            }
        }

        vector<vector<int>> out;
        for (std::array<int,4> vec : res) {
            out.push_back(std::vector<int>(vec.begin(), vec.end()));
        }
        return out;
    }
};