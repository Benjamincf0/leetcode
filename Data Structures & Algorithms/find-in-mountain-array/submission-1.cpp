/**
 * // This is the MountainArray's API interface.
 * // You should not implement it, or speculate about its implementation
 * class MountainArray {
 *   public:
 *     int get(int index);
 *     int length();
 * };
 */

class Solution {
public:
    int findInMountainArray(int target, MountainArray &mountainArr) {
        // triple binary search
        // if (mountainArr.get(0) == target) return 0;

        int l = 1;
        int r = mountainArr.length()-1;
        int mid;
        while (l<=r) {
            mid = (l+r)/2;
            int midVal = mountainArr.get(mid);
            int slope_left = midVal-mountainArr.get(mid-1);

            if (slope_left > 0) {
                if (mountainArr.get(mid+1)-midVal < 0) break;
            }
            
            if (slope_left > 0) {
                l = mid;
            } else {
                r = mid;
            }
        }

        std::cout << mid << std::endl;
        int summit = mid;

        l = 0;
        r = summit;
        while (l<=r) {
            mid = (l+r)/2;
            int midVal = mountainArr.get(mid);

            if (midVal == target) {
                return mid;
            } else if (midVal < target) {
                l = mid+1;
            } else {
                r = mid-1;
            }
        }

        l = summit+1;
        r = mountainArr.length()-1;
        while (l<=r) {
            mid = (l+r)/2;
            int midVal = mountainArr.get(mid);

            if (midVal == target) {
                return mid;
            } else if (midVal < target) {
                r = mid-1;
            } else {
                l = mid+1;
            }
        }

        return -1;
    }
};