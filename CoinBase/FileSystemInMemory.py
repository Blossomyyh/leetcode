"""
588. Design In-Memory File System

defaultdict --- no need to check empty path


1. replication -- data duplication async
    move data close to users

2. sharding -- data partitioning
    based on user location

3. distributed system
    mapreduce here to process distributed dataset e#iciently
    map function —> key-value pairs —> shu%es —> reduce functions —> transfer to meaningful datasets

4. cache

5. concurrent controll -- lock mechanism when writing or reading files

6. garbage collection
     orphaned blobs that are basically unused and taking up storage for no reason.

"""

from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.content = ""


class FileSystem:
    def __init__(self):
        self.root = TrieNode()

    # find and return node at path
    def _getDirectory(self, path):
        if len(path)== 1:
            return self.root
        paths = path.split('/')[1:]

        node = self.root
        for p in paths:
            node = node.children[p]

        return node

    def ls(self, path: str) -> [str]:
        node = self._getDirectory(path)
        if node.content:
            # file path
            # return file name
            return [path.split('/')[-1]]
        else:
            # if path is empty will return []
            return sorted(node.children.keys())

    def mkdir(self, path: str) -> None:
        self._getDirectory(path)


    def addContentToFile(self, filePath: str, content: str) -> None:

        node = self._getDirectory(filePath)
        node.content += content


    def readContentFromFile(self, filePath: str) -> str:
        node = self._getDirectory(filePath)
        return node.content

    # Your FileSystem object will be instantiated and called as such:
    # obj = FileSystem()
    # param_1 = obj.ls(path)
    # obj.mkdir(path)
    # obj.addContentToFile(filePath,content)
    # param_4 = obj.readContentFromFile(filePath)