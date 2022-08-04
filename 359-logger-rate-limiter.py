class Logger:

    def __init__(self):
        self.ts_map = {}
        self.so_far = set()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:

        for key in list(self.ts_map.keys()):
            if key + 10 <= timestamp:
                self.so_far = self.so_far - self.ts_map.pop(key)

        if message in self.so_far:
            return False

        self.so_far.add(message)
        self.ts_map[timestamp] = self.ts_map.get(timestamp, set())
        self.ts_map[timestamp].add(message)
        return True

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
