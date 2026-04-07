class MinStack:

    def __init__(self):
        self._stack = []
        self._min = float('inf')

    def push(self, val: int) -> None:
        if not self._stack:
            self._stack.append(0)
            self._min = val
            return

        self._stack.append(val - self._min)
        self._min = min(val, self._min)

    def pop(self) -> None:
        encoded = self._stack.pop()
        if encoded < 0: # meaning that it was less than the min when it was added
            # so actual value is min
            # encoded = num - prev_min && self._min = num
            # prev_min = num - encoded = self._min - encoded
            decoded = self._min
            self._min = self._min - encoded # self._min = prev_min
        else:
            decoded = encoded+self._min
        
        return decoded

    def top(self) -> int:
        encoded = self._stack[-1]
        if encoded < 0: return self._min
        else: return encoded + self._min


    def getMin(self) -> int:
        return self._min