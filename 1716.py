class Solution:
    def totalMoney(self, n: int) -> int:
        # sum(i -> n){i}
        # Ex n = 25
        # 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28
        # 2 + 3 + 4 + 5 + 6 + 7 + 8 = 28 + 7
        # 3 + 4 + 5 + 6 + 7 + 8 + 9 = 28 + 7*2
        # 4 + 5 + 6 + 7
        numOfWeeks = n // 7
        sumFullWeeks = numOfWeeks*28 + (7*numOfWeeks*(numOfWeeks-1)) // 2

        numDaysLeft = n % 7
        lastMondayAmount = numOfWeeks
        sumDaysLeft = 0
        for i in range(numDaysLeft):
            sumDaysLeft += i + numOfWeeks + 1

        return sumFullWeeks + sumDaysLeft