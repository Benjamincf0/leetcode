class Solution {
public:
    int trib(std::unordered_map<int, int>& cache, int n) {

        if (cache.contains(n)) return cache[n];
        
        cache[n] = trib(cache, n-1)+trib(cache, n-2)+trib(cache,n-3);
        return cache[n];
    }
    int tribonacci(int n) {
        if (n < 2) return n;
        if (n == 2) return 1;
        int n_3 = 0;
        int n_2 = 1;
        int n_1 = 1;

        for (int i = 2; i < n; i++) {
            int n = n_1 + n_2 + n_3;
            // std::cout << n_1 << ' ' << n_2 << ' ' << n_3 << '\n';
            n_3 = n_2;
            n_2 = n_1;
            n_1 = n;
        }

        return n_1;
    }
};