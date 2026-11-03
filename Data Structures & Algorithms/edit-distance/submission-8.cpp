class Solution {
public:
    int minDistance(string word1, string word2) {
        if (word1.size() > word2.size()) {
            string temp = word1;
            word1 = word2;
            word2 = temp;
        }
        std::vector<int> dp_prev(word1.size()+1);
        std::vector<int> dp_cur(word1.size()+1);

        for (int i=0; i < word1.size()+1; i++) {
            dp_prev[i] = word1.size()-i;
        }

        for (int i=word2.size()-1; i >= 0; i--) {
            dp_cur[word1.size()] = word2.size()-i;
            for (int j=word1.size()-1; j >= 0; j--) {
                if (word1[j] == word2[i]) {
                    dp_cur[j] = dp_prev[j+1];
                } else {
                    std::vector<int> els = {1+dp_prev[j+1],
                                        1+dp_cur[j+1],
                                        1+dp_prev[j]};
                    dp_cur[j] = *std::min_element(
                                          els.begin(),
                                          els.end()
                                        );
                }
            }
            dp_prev = dp_cur;
        }
        return dp_prev[0];
    }
};