def is_balanced(n: int) -> bool:
    map = {}
    for d in str(n):
        num = int(d)
        if not map.get(num):
            map[num] = 1
        else:
            map[num] += 1
    
    for key, val in map.items():
        if key != val:
            return False

    return True

lt = []
i = 0
while i <= 122:
    if is_balanced(i): lt.append(i)
    i += 1

class Solution:

    def nextBeautifulNumber(self, n: int) -> int:
        left = 0
        right = len(lt) - 1
        mid = 0
        while left < right:
            mid = (left + right) // 2
            val = lt[mid]
            if n > val:
                left = mid + 1
            elif n < val:
                right = mid - 1
            else: return lt[mid + 1]
        return lt[right]
