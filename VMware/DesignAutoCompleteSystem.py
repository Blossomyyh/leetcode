class Trie:
    def __init__(self):
        self.words = None
        self.fre = 0
        self.children = {}

import heapq
class AutocompleteSystem:
    def __init__(self, sentences: [str], times: [int]):
        self.root = Trie()
        self.keyword = ""

        # build trie
        for item, times in zip(sentences, times):
            self._addRecord(item, times)


    def _addRecord(self, item, times):
        node = self.root
        for c in item:
            if c not in node.children:
                node.children[c] = Trie()
            node = node.children[c]
        node.words = item
        node.fre -= times

    def _dfs(self, root):
        ret = []
        if root:
            if root.words:
                ret.append((root.fre, root.words))
            for child in root.children:
                ret.extend(self._dfs(root.children[child]))
        return ret

    def _search(self, sentence):
        node = self.root
        for c in sentence:
            if c not in node.children:
                return []
            node = node.children[c]
        return self._dfs(node)



    def input(self, c: str) -> [str]:

        res = []
        if c != "#":
            self.keyword += c
            res = self._search(self.keyword)
        else:
            self._addRecord(self.keyword, 1)
            self.keyword = ""
        # res here is reusable --> need to use sorted
        return [item[1] for item in sorted(res)[:3]]
