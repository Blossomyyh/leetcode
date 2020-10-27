"""
214. Shortest Palindrome

Example: s = dedcba. Then r = abcded and
I try these overlays
(the part in (...) is the prefix I cut off,
 I just include it in the display for better understanding):
"""
def shortestPalindrome(s):
    r = s[::-1]
    for i in range(1, len(r)+1):
        # s.startswith return T/F
        # already reverse --> make sure s[i:] is palindrom with r[:i]
        # only need veryfy r[i:]
        if s.startswith(r[i:]):
            return r[:i]+s

  # s          dedcba
# r --
  # r[0:]      abcded    Nope...
  # r[1:]   (a)bcded     Nope...
  # r[2:]  (ab)cded      Nope...
  # r[3:] (abc)ded       Yes! Return abc + dedcba