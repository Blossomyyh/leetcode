"""
Output: "apple"
Explanation:
Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".

"""

"""
\\ sort and check

sort by the length, and then by string
so that we can get the largest word first --> reduce time

time : O(n^2)
\\ create substring cost n^2 + set space
space: O(n^2)
"""
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
from typing import List
def longestWord(words: List[str]) -> str:
    if not words: return ""
    if len(words) == 1: return words[0]
    wordset = set(words)
    words.sort(key=lambda x: (-len(x), x))

    def checksub(word):
        for i in range(len(word)):
            if word[0:i + 1] not in wordset:
                return False
        return True

    for word in words:
        print(word)
        if checksub(word): return word
    return ""

# print(longestWord(words))



"""
\\ 2. trie
wo, wow

start from a, b
traversal subtrie after a/b
for each level find whether there a #
w
|
o
/\
w #
"""
def lwdTrie(words):
    trieDic = {}
    for word in words:
        node  = trieDic
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node['#'] = word

    print(trieDic)

#     traversal the trie and record the longest word that each level has is a word in dic

    def dfs(node, prev):

        if '#' not in node:
            return prev
        prev = node['#']
        print(node, "node", prev)
        keylist = list(node.keys())
        keylist.sort()
        """sort() cannot return a list --> write seperate keylist.sort() for sorting"""
        for key in keylist:
            if key=='#':
                continue
            else:
                return dfs(node[key], prev)

        return prev
    res = ""
#     DFS longest path
    for key in trieDic:
        node = trieDic[key]
        # node has another dictionary structure-> key is the next ch or #
        longword = dfs(node, "")
        print(longword, "long")
        if len(longword) > len(res):
            res = longword
        elif len(longword) == len(res) and longword < res:
            res = longword
    return res



print(lwdTrie(words))

dic = {'a': {'#': 'a',
             'p':
                 {'p':
                      {'#': 'app',
                       'l': {'#': 'appl',
                             'y': {'#': 'apply'},
                             'e': {'#': 'apple'}
                             }
                       },
                  '#': 'ap'}
             },
       'b': {'a':
                 {'n':
                      {'a':
                           {'n':
                                {'a':
                                     {'#': 'banana'}
                                 }
                            }
                       }
                  }
             }
       }


class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.end = False


class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        root = TrieNode()

        """\\ sorted string !!!!\\ """
        words = sorted(set(words), key=lambda word: (-len(word), word))
        #      1. length greater, move ahead 2. lexicographically less, move forward

        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.end = True

        # start from longest and lexi less word
        for word in words:
            node = root
            flag = True
            for ch in word:
                if node.children[ch].end == False:
                    flag = False
                    break
                else:
                    node = node.children[ch]
            if flag:
                return word

        return ''