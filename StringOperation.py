"""
String Operation

##### RE ###########
A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.

# findall # - list
Returns a list containing all matches

# split # - list
Returns a list where the string has been split at each match

# search # -> Match Obj  -- only search for first occurrence
Returns a Match object if there is a match anywhere in the string

        ==== Match Object ====
        # x.span()
        # x.group()
        # x.end() end index of match
        # x.start() start index of match
        # x.string

# sub # - replace
Replaces one or many matches with a string


# full match # re.fullmatch(patter, string, flag)
    pattern = "(" + str1[0:div] + ")+"
    if re.fullmatch(pattern, str1

"""

import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x.span(), x.start(), x.end(), ", string:", x.string, ", group: ", x.group())

txt = "Ahh The rain in Spain"
x = re.search("[T]he.+Spain$", txt)
print(x.span(), x.start(), x.end(), ", string:", x.string, ", group: ", x.group())

# Match Object
# The Match object has properties and methods used to retrieve information about the search, and the result:
#
# .span() returns a tuple containing the start-, and end positions of the match.
# .string returns the string passed into the function
# .group() returns the part of the string where there was a match

"""
Metacharacters
    Metacharacters are characters with a special meaning:

[]	A set of characters	\\ "[a-m]"	
\	Signals a special sequence (can also be used to escape special characters)	\\ "\d"	
.	Any character (except newline character) \\	"he..o"	
^	Starts with	 \\ "^hello"	
$	Ends with	\\ "world$"	
*	Zero or more occurrences	\\ "aix*"	
+	One or more occurrences	\\ "aix+"	
{}	Exactly the specified number of occurrences	 \\ "al{2}"	
|	Either or	\\ "falls|stays"	
()	Capture and group

"""

"""
Set

[arn]	Returns a match where one of the specified characters (a, r, or n) are present	
[a-n]	Returns a match for any lower case character, alphabetically between a and n	
[^arn]	Returns a match for any character EXCEPT a, r, and n	
[0123]	Returns a match where any of the specified digits (0, 1, 2, or 3) are present	
[0-9]	Returns a match for any digit between 0 and 9	
[0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59	
[a-zA-Z]	Returns a match for any character alphabetically between a and z, lower case OR upper case	
[+]	In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string

"""

"""
Special Sequences
   A special sequence is a \ followed by one of the characters in the list below, and has a special meaning:
   
\A	Returns a match if the specified characters are at the beginning of the string	\\ "\AThe"	
\b	Returns a match where the specified characters are at the beginning or at the end of a word
(the "r" in the beginning is making sure that the string is being treated as a "raw string")  \\	r"\bain"
r"ain\b"	
\B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
(the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\Bain"
r"ain\B"	
\d	Returns a match where the string contains digits (numbers from 0-9)	"\d"	
\D	Returns a match where the string DOES NOT contain digits	"\D"	
\s	Returns a match where the string contains a white space character	"\s"	
\S	Returns a match where the string DOES NOT contain a white space character	"\S"	
\w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	"\w"	
\W	Returns a match where the string DOES NOT contain any word characters	"\W"	
\Z	Returns a match if the specified characters are at the end of the string


"""

"""
Quantifiers

Quantifier	Legend	Example	Sample Match
+	One or more	Version \w-\w+	Version A-b1_1
{3}	Exactly three times	\D{3}	ABC
{2,4}	Two to four times	\d{2,4}	156
{3,}	Three or more times	\w{3,}	regex_tutorial
*	Zero or more times	A*B*C*	AAACC
?	Once or none	plurals?	plural


Logic	Legend	Example	Sample Match

|	Alternation / OR operand	22|33	33
( … )	Capturing group	A(nt|pple)	Apple (captures "pple")
\1	Contents of Group 1	r(\w)g\1x	regex
\2	Contents of Group 2	(\d\d)\+(\d\d)=\2\+\1	12+65=65+12
(?: … )	Non-capturing group	A(?:nt|pple)	Apple


https://www.rexegg.com/regex-quickstart.html

\n	Line feed character	see below	
\r\n	Line separator on Windows	AB\r\nCD	AB
CD
\
"""




#######
# contains white space \s
txt = "The rain in Spain"
x = re.search("\s", txt)
print(x)
# if not x:
#     print(x)

# "r" in the beginning is making sure that the string is being treated as a "raw string")
print("\s :", x.span())

# Split at each white-space character:
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

# Print the position (start- and end-position) of the first match occurrence.
# The regular expression looks for any words that starts with an upper case "S":
txt = "The rain in Spain Set"
x = re.findall(r"\bS\w+", txt)
print(x)

# sub --- replace
txt = "The rain in Spain"
# You can control the number of replacements by specifying the count parameter:
x = re.sub("\s", "9", txt, 2)
print(x)
