from typing import List
import collections
"""
1. domain
811. Subdomain Visit Count

deal with string
init a dictionary to store all domains and counts accordingly
split each string to get count and whole domain name-> split to subdomain
add counts to dictionary
output dictionary
"""
def subdomainVisits(cpdomains: List[str]) -> List[str]:
    dictionary = {}
    for cpdomain in cpdomains:
        splitString = cpdomain.split(' ')
        count = int(splitString[0])
        domain = splitString[1]
        subdomain = domain.split('.')
        for i in range(len(subdomain)):
            key = ".".join(subdomain[i:])
            dictionary[key] = dictionary.get(key, 0) + count

    result = []
    for key, value in dictionary.items():
        newString = str(value) + " " + key
        result.append(newString)
    return result

# simpler way of domain
def subdomainVisits(cpdomains):
    ans = collections.Counter()
    for domain in cpdomains:
        count, domain = domain.split()
        count = int(count)
        frags = domain.split('.')
        for i in range(len(frags)):
            ans[".".join(frags[i:])] += count

    return ["{} {}".format(ct, dom) for dom, ct in ans.items()]





#################################
def parser(s):
    subdomain = s.split('.')[::-1]
    res = []
    for sub in subdomain:
        if not res:
            res.append(sub)
            continue
        res.append('{}.{}'.format(sub, res[-1]))
    return res

def clicker_counter(clicker):
    d = {}
    for entry in clicker:
        keys = parser(entry[0])
        for key in keys:
            d[key] = d.get(key, 0) + int(entry[1])

    return [[k, str(v)] for k, v in d.items()]

def parser_(s):
    res = []
    s = s[0].split('.')[::-1]
    for string in s:
        if not res:
            res.append(string)
        else:
            res.append("{}.{}".format(string, res[-1]))
    return res

def clicker_counter_(clicker):
    res = {}
    for history in clicker:
        keys = parser_(history)
        val = history[1]
        for k in keys:
            res[k] = res.get(k, 0) + int(val)
    return res

# print(parser("sports.yahoo.com"))
test1 = [
    ["google.com", "60"],
    ["yahoo.com", "50"],
    ["sports.yahoo.com", "80"]
]

print(clicker_counter(test1))
print(clicker_counter_(test1))



#############
# domain 3

