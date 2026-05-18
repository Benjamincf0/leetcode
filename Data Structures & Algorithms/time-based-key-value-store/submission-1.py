class TimeMap:

    def __init__(self):
        self._user_records: dict[str, list[tuple[str, int]]] = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        record = (value, timestamp)
        self._user_records[key].append(record)

    def get(self, key: str, timestamp: int) -> str:
        records = self._user_records[key]

        l, r = 0, len(records)-1

        mid_left = ""
        while l<=r:
            mid = (l+r)//2
            mid_timestamp = records[mid][1]

            if mid_timestamp == timestamp: return records[mid][0]
            elif mid_timestamp > timestamp:
                r = mid-1
            else:
                l = mid+1
                mid_left = records[mid][0]

        return mid_left