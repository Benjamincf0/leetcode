class Solution {
public:
    int trib(std::unordered_map<int, int>& cache, int n) {
        if (n < 2) return n;
        if (n == 2) return 1;

        if (cache.contains(n)) return cache[n];
        
        cache[n] = trib(cache, n-1)+trib(cache, n-2)+trib(cache, n-3);
        return cache[n];
    }
    int tribonacci(int n) {
        std::unordered_map<int, int> cache;
        return trib(cache, n);
    }
};