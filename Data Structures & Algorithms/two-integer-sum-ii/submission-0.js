class Solution {
    /**
     * @param {number[]} numbers
     * @param {number} target
     * @return {number[]}
     */
    twoSum(numbers, target) {
        let i = 0;
        let j = numbers.length-1;

        while (i < j) {
            const n1 = numbers[i];
            const n2 = numbers[j];
            const sum = n1+n2;

            if (sum > target) {
                j--;
            } else if (sum < target) {
                i++;
            } else {
                return [++i, ++j];
            }
        }
    }
}
