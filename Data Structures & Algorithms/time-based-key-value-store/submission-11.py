class TimeMap:

    def __init__(self):
        self.TimeStamps = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.TimeStamps[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:

        res = ""

        if key not in self.TimeStamps:
            return res
        
        log = self.TimeStamps[key]

        l,r = 0, len(log) - 1

        while l <= r:

            m = (l + r) // 2

            if log[m][1] > timestamp:
                r = m - 1
            else:
                res = log[m][0]
                l += 1
        
        return res

        
