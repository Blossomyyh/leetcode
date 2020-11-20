"""
Implement the LogSystem class:

LogSystem() Initializes the LogSystem object.

void put(int id, string timestamp)
    Stores the given log (id, timestamp) in your storage system.

int[] retrieve(string start, string end, string granularity)

    For example, start = "2017:01:01:23:59:59", end = "2017:01:02:23:59:59", and granularity = "Day"
    means that we need to find the logs within the inclusive
     range from Jan. 1st 2017 to Jan. 2nd 2017,
     and the Hour, Minute, and Second for each log entry can be ignored.

"""
class LogSystem:
    def __init__(self):
        self.logs = []

    def put(self, id: int, timestamp: str) -> None:
        self.logs.append((id, timestamp))

    """
    Returns the IDs of the logs whose timestamps are within the range from start to end inclusive.
    start and end all have the same format as timestamp,
    and granularity means how precise the range should be
    (i.e. to the exact Day, Minute, etc.).

    """
    def retrieve(self, start: str, end: str, granularity: str) -> [int]:
        index = {
            'Year': 5,
            'Month': 8,
            'Day': 11,
            'Hour': 14,
            'Minute': 17,
            'Second': 20
        }[granularity]

        """ \\ use dictionary to get the range """
        s = start[:index]
        e = end[:index]
        res = [idx for idx, time in self.logs if s<=time[:index]<=e ]
        return sorted(res)





        # Your LogSystem object will be instantiated and called as such:
        # obj = LogSystem()
        # obj.put(id,timestamp)
        # param_2 = obj.retrieve(start,end,granularity)