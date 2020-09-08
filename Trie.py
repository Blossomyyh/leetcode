class TrieNode:
    def __init__(self):
        self.childNodes = {}
        self.isWordEnd = False


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        currNode = self.root
        for ch in word:
            node = currNode.childNodes.get(ch, TrieNode())
            currNode.childNodes[ch] = node
            currNode = node
        currNode.isWordEnd = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        currNode = self.root
        for ch in word:
            node = currNode.childNodes.get(ch)
            if not node:
                return False
            else:
                currNode = node
        return currNode.isWordEnd

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        currNode = self.root
        for ch in prefix:
            node = currNode.childNodes.get(ch)
            if not node:
                return False

            currNode = node
        return True



        # Your Trie object will be instantiated and called as such:
        # obj = Trie()
        # obj.insert(word)
        # param_2 = obj.search(word)
        # param_3 = obj.startsWith(prefix)