class MinStack:

    def __init__(self):
        self._l = []
        self._min_prefix = []

    def push(self, val: int) -> None:
        self._l.append(val)
        if len(self._min_prefix)>0: _min = min(val, self._min_prefix[-1])
        else: _min = val
        self._min_prefix.append(_min)

    def pop(self) -> None:
        self._min_prefix.pop()
        return self._l.pop()

    def top(self) -> int:
        return self._l[-1] if len(self._l)>0 else None

    def getMin(self) -> int:
        return self._min_prefix[-1] if len(self._min_prefix)>0 else None