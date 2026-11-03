class Solution {
public:
    uint64_t hash_coords(uint32_t x, uint32_t y) {
        return (static_cast<uint64_t>(x)) << 32 | y;
    }
    uint32_t dfs(int i, int j, string& word1, string& word2, std::unordered_map<uint64_t,int>& memo) {
            if (i == word1.size() && j == word2.size()) {
                return 0;
            } else if (i == word1.size() || j == word2.size()) {
                return std::max(word1.size()-i,word2.size()-j);
            }
            
            if (memo.contains(hash_coords(i,j))) {
                return memo.at(hash_coords(i,j));
            }

            if (word1[i] == word2[j]) {
                memo.emplace(hash_coords(i,j),                       
                    dfs(i+1,j+1,word1,word2,memo));
            } else {
                memo.emplace(hash_coords(i,j), 
                    std::min(
                        1+dfs(i,j+1,word1,word2,memo),std::min( // insert
                        1+dfs(i+1,j,word1,word2,memo), // delete
                        1+dfs(i+1,j+1,word1,word2,memo) // replace
                    )));
            }

            return memo.at(hash_coords(i,j));
    }
    int minDistance(string word1, string word2) {
        std::unordered_map<uint64_t,int> memo = {};
        return dfs(0,0,word1,word2,memo);
    }
};
