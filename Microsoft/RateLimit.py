"""
359. Logger Rate Limiter

1. check in dic -->(1) >= 10s true+update (2) < false+no-update
2. not in dic true + update
"""
class Logger:
    def __init__(self):
        self.dict = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
                Returns true if the message should be printed in the given timestamp, otherwise returns false.
                If this method returns false, the message will not be printed.
                The timestamp is in seconds granularity.
        """
        if message not in self.dict:
            self.dict[message] = timestamp
            return True

        if timestamp-self.dict[message] >= 10:
            self.dict[message] = timestamp
            return True
        else:
            return False
