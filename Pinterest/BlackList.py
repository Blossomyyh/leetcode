"""
black list  ----   pintext safe

given a phrase list, and a sentense
print out the phrase occurs in the sentense
"""
"""
trie a tree to store several string cha by cha
aw, aws
a
\
 w - end
 \
 s - end

Trie based on phrases
s"i am good"
p"i am"
search the sentence find the cha in root keys
   do dfs start from cha 
   def dfs(idx, node):
        if node.end = true
            return end phrase
        if idx->cha in node key:
            node = node[key]
            dfs(idx+1, node)
        else：
            :return

time : O(n^2)
space : O(n)
"""


worddict = ['I am good', 'I am', 'handsome']
sentence = 'I am good and handsome'

a = {'I': {' ':
               {'a':
                    {'m': {'#': 'I am'}}
                }
           },
     'h':
         {'a':
              {'n':
                   {'d': {'s': {'o': {'m': {'e': {'#': 'handsome'}}}}}}}}}
def blacklist(worddict, sentence):
    # build trie
    trie = {}
    for word in worddict:
        node = trie
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node['#'] = word
    print(trie)

    result = []
    def dfs(idx, node):
        if '#' in node:
            result.append(node['#'])
        if idx<len(sentence) and sentence[idx] in node:
            node = node[sentence[idx]]
            dfs(idx+1, node)

    for i in range(len(sentence)):
        if sentence[i] in trie:
            dfs(i+1, trie[sentence[i]])

    return result
print(blacklist(worddict, sentence))
