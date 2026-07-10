class TimeMap:

    def __init__(self):
        self.dic = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        vals = self.dic.get(key, [])
        if not vals:
            return ""
        low = 0
        high = len(self.dic[key])-1
        while low<=high:
            mid = (low+high)//2
            if vals[mid][0] <= timestamp:
                res = vals[mid][1]
                low = mid+1
            else:
                high = mid-1
        return res
        
