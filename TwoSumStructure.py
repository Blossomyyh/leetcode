""""dictionary"""

class TwoSum:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.num = {}

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.num[number] = self.num.get(number, 0) + 1

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for n in self.num.keys():
            if value - n != n and value - n in self.num.keys():
                return True
            elif value - n == n and self.num[n] > 1:
                return True
        return False



        # Your TwoSum object will be instantiated and called as such:
        # obj = TwoSum()
        # obj.add(number)
        # param_2 = obj.find(value)

"""sorted list"""

class TwoSum:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.num = []

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.num.append(number)

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        self.num.sort()
        s, e = 0, len(self.num) - 1
        while s < e < len(self.num):
            if self.num[s] + self.num[e] == value:
                return True
            elif self.num[s] + self.num[e] < value:
                s += 1
        pass