class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = [[0]*(len(num1)+len(num2)) for _ in range(len(num1))]
        final_res = []
        for i1, n1 in enumerate(num1[::-1]):
            n1 = ord(n1)-ord('0')
            carry = 0
            i2 = 0
            for i2, n2 in enumerate(num2[::-1]):
                n2 = ord(n2)-ord('0')

                p = n1*n2+carry
                s = p % 10
                res[i1][i1+i2] = s
                carry = p // 10

            if carry != 0: res[i1][i1+i2+1] = carry

        carry = 0
        for i in range(len(res[0])):
            s = sum(arr[i] for arr in res) + carry
            final_res.append(s % 10)
            carry = s // 10

        # print(num2)
        # print(num1)
        # print()
        # for arr in res:
        #     print(''.join(str(i) for i in arr[::-1]))
        # print(''.join(str(i) for i in final_res[::-1]))

        while final_res and final_res[-1] == 0: final_res.pop()

        out = "".join(str(n) for n in final_res[::-1])
        return out if out else "0"