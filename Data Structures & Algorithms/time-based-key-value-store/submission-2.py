class TimeMap:

    def __init__(self):
        self.Timestamps = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.Timestamps[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key not in self.Timestamps:
            return res
        
        log = self.Timestamps[key]

        l,r = 0, len(log) - 1

        while l <= r:
            m = (l + r) // 2

            if log[m][-1] <= timestamp:
                res = log[m][0]
                l = m + 1
            else:
                r = m - 1
        
        return res
        

