class TimeMap:

    def __init__(self):
        self.match = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.match:
            self.match[key] = []
        self.match[key].append([value,timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        values = self.match.get(key,[])
    
        l , r = 0, len(values)-1
        while l<=r:
            m = (l+r)//2
            if values[m][1] <= timestamp:
                l = m+1
            else:
                r = m-1
        return "" if r == -1 else values[r][0];

        
