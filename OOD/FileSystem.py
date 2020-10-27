"""
bool createPath(string path, int value) Creates a new path and associates a value to it if possible and returns true. Returns false if the path already exists or its parent path doesn't exist.
int get(string path) Returns the value associated with path or returns -1 if the path doesn't exist.
"""

from collections import defaultdict
class Trie:
    def __init__(self, val):
        self.root = defaultdict(Trie)
        self.val = val
    def find(self, path):
        cur = self.root
        for p in path:
            if p not in cur:
                return None
            else:
                cur = cur[p]
        return cur
    def insert(self, val, path):
        node = self.find(path[:-1])
        if not node:
            return False
        else:
            if path[-1] in node:
                return False
            else:
                node[path[-1]] = Trie(val)
                return True


class FileSystem:
    def __init__(self):
        self.root = Trie(0)

    def createPath(self, path: str, value: int) -> bool:
        pathlis = path.split('/')[1:]
        return self.root.insert(pathlis,value)

    def get(self, path: str) -> int:
        pathlis = path.split('/')[1:]
        n = self.root.find(pathlis)
        if not n:
            return -1
        else:
            return n.val



# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)

class Trie:
    def __init__(self, val):
        self.root = defaultdict(Trie)
        self.val = val

    def find(self, pathLis):
        curr = self
        for ch in pathLis:
            if ch not in curr.root:
                return None
            curr = curr.root[ch]
        return curr

    def insert(self, pathLis, val):
        node = (self.find(pathLis[:-1]))
        if not node or pathLis[-1] in node.root:
            return False
        node.root[pathLis[-1]] = Trie(val)
        return True