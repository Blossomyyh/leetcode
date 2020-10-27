"""
17. Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Pseudo code:
assume input is valid, only contains digits from 2-9
create a mapping for number and according characters like 2->['a', 'b', 'c']
bactracking recursive function
  \\ backtrack(combination, next_digits) which takes as arguments an ongoing letter combination and the next digits to check.

1.If there is no more digits to check that means that the current combination is done.

2.If there are still digits to check :
    Iterate over the letters mapping the next available digit.
    Append the current letter to the current combination combination = combination + letter.
    Proceed to check next digits : backtrack(combination + letter, next_digits[1:]).

"""

from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapDigits = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z']
        }


        def backtracking(remainDigit, combination):
            # bottom case
            if len(remainDigit) == 0:
                result.append(combination)
                return
            firstDigit = int(remainDigit[0])
            if firstDigit in mapDigits:
                for ch in mapDigits[firstDigit]:
                    """ 
                    never assign new value to a string in backtracking!!!!! - pass the new value back as well!!
                    """
                    backtracking(remainDigit[1:], combination + ch)

        result = []
        if len(digits) > 0:
            backtracking(digits, "")
        else:
            return []
        return result

print(Solution().letterCombinations("23"))

