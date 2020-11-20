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

            """start from [i:] then we can get the right subdomains"""
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
    print(s)
    for string in s:
        if not res:
            res.append(string)
        else:
            res.append("{}.{}".format(string, res[-1]))
    print(res)
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

# print(clicker_counter(test1))
print(clicker_counter_(test1))



#############
# domain 3
# 给了三个list，第一个是purchase的userid list,
# 第二个是广告click记录，每一条是[ IP address, AD],
# 第三个是userid, IP对照表，
# 然后问对每条ad来说，# of purchase/ # of click。
# 还有些别的假设：每个用户只有一次purchase，每个用户只有一个ip



###3
completed_purchase_user_ids = [
    "3123122444", "234111110", "8321125440", "99911063"]

ad_clicks = [
    ##userID, time, product
    "122.121.0.1,2016-11-03 11:41:19,Buy wool coats for your pets",
    "96.3.199.11,2016-10-15 20:18:31,2017 Pet Mittens",
    "122.121.0.250,2016-11-01 06:13:13,The Best Hollywood Coats",
    "82.1.106.8,2016-11-12 23:05:14,Buy wool coats for your pets",
    "92.130.6.144,2017-01-01 03:18:55,Buy wool coats for your pets",
    "92.130.6.145,2017-01-01 03:18:55,2017 Pet Mittens",
]

all_user_ips = [
    ##"User_ID,IP_Address",
    "2339985511,122.121.0.250",
    "234111110,122.121.0.1",
    "3123122444,92.130.6.145",
    "39471289472,96.3.199.11",
    "8321125440,82.1.106.8",
    "99911063,92.130.6.144"
]


##dic1 =  {ipAddress:userID}
##dic2 = {product:[totalClickTimes, purchasedTime]}

def task3(completed_purchase_user_ids, ad_clicks, all_user_ips):
    ipToId = {}
    productInfo = {}
    completed_purchase_user_ids = set(completed_purchase_user_ids)
    for info in all_user_ips:
        userId, ip = info.split(",")
        ipToId[ip] = userId
    for info in ad_clicks:
        ip, _, product = info.split(",")
        if product not in productInfo:
            productInfo[product] = [0, 0]
        productInfo[product][0] += 1
        if ipToId[ip] in completed_purchase_user_ids:
            productInfo[product][1] += 1
    return productInfo

# {'Buy wool coats for your pets': [3, 3], '2017 Pet Mittens': [2, 1], 'The Best Hollywood Coats': [1, 0]}
# {product:[totalClickTimes, purchasedTime]}
print(task3(completed_purchase_user_ids, ad_clicks, all_user_ips))
