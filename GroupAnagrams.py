from typing import List
from collections import defaultdict
"""
group anagrams
1. dictionary to store a key for all words have same characters
2. key - string a sorted one. we can make sure one group only has one key
3. traversal the list and store them by the key
4. print out values in dic
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for item in strs:
            # sort the character alphabetically
            key = "".join(sorted(item)).lower()
            dic[key].append(item)
        return dic.values()