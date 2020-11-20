class Bucket:
    def __init__(self):
        # element (key, value)
        self.bucket = []
    def get(self, key):
        for k,v in self.bucket:
            if k == key:
                return v
        return -1
    def update(self, key, value):
        found = False
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                """tuple does not support value assignment"""
                self.bucket[i] = (key, value)
                found = True
                break
        if not found:
            self.bucket.append((key, value))
    def remove(self, key):
        for i, kv in enumerate(self.bucket):
            if key==kv[0]:
                # del by index
                del self.bucket[i]


class MyHashMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # better to be a prime number, less collision
        self.keyspace = 2069
        self.hashtable = [Bucket() for i in range(self.keyspace)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        hashkey = key % self.keyspace
        self.hashtable[hashkey].update(key, value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hashkey = key % self.keyspace
        return self.hashtable[hashkey].get(key)

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        hashkey = key % self.keyspace
        self.hashtable[hashkey].remove(key)


        # Your MyHashMap object will be instantiated and called as such:
        # obj = MyHashMap()
        # obj.put(key,value)
        # param_2 = obj.get(key)
        # obj.remove(key)

