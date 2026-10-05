class Solution {
    /**
     * @param {number} a
     * @param {number} b
     * @return {number}
     */
    getSum(a: number, b: number): number {
        let mask = 0xffffffff
        while (b != 0) {
            let carry = ((a & b) << 1) & mask
            a = a ^ b
            b = carry
        }

        return (a<=0x7fffffff)?a:~(a ^ mask)
    }
}
