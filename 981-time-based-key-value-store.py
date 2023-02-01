class TimeMap:

    def __init__(self):
        self._map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self._map[key] = self._map.get(key, [])
        self._map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self._map or timestamp < self._map[key][0][0]:
            return ""

        ls = self._map[key]
        start, end = 0, len(ls) - 1

        while start <= end:
            mid = int(end - (end - start) / 2)
            if ls[mid][0] <= timestamp:
                if mid + 1 == len(ls) or ls[mid + 1][0] > timestamp:
                    return ls[mid][1]

                start = mid + 1

            else:
                end = mid - 1

        return ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

