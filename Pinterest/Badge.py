"""
badge question

1.

"exit enter"
"""
test1 = [
    ["Martha", "exit"],
    ["Paul", "enter"],
    ["Martha", "enter"],
    ["Martha", "exit"],
    ["Jennifer", "enter"],
    ["Paul", "enter"],
    ["Curtis", "enter"],
    ["Paul", "exit"],
    ["Martha", "enter"],
    ["Martha", "exit"],
    ["Jennifer", "exit"]
]


test2 = [
    ["Paul", 1355],
    ["Jennifer", 1910],
    ["John", 830],
    ["Paul", 1315],
    ["John", 835],
    ["Paul", 1405],
    ["Paul", 1630],
    ["John", 855],
    ["John", 915],
    ["John", 930],
    ["Jennifer", 1335],
    ["Jennifer", 730],
    ["John", 1630]
]

from collections import defaultdict
def badge1(entrylist):
    dic = defaultdict(list)
    for per, status in entrylist:
        dic[per].append(status)

    enterwithout = set()
    exitwithout = set()
    for p, record in dic.items():
        stack = []
        for i in record:
            if i == "enter":
                stack.append(i)
            else:
                if not stack:
                    enterwithout.add(p)
                elif stack[-1] == "enter":
                    stack.pop()
        if stack:
            exitwithout.add(p)
    print("enter without badge:",list(enterwithout))
    print("exit without badge:",list(exitwithout))



"""
collect all the time of one person -> dictionary
for each person:
    sort the time
    for each time:
        count idx points to 1h later
        if idx - curtimeidx >=3:
        result append this list
        
"""
def badge2(badge_record):
    dic = defaultdict(list)
    for person, record in badge_record:
        dic[person].append(record)
    result = defaultdict(list)
    for person, record in dic.items():
        record.sort()
        for idx, time in enumerate(record):
            if len(record)>=3:
                endtime = time + 100
                i = idx +1
                while i < len(record) and record[i]<=endtime:
                    i+= 1

                if i-idx+1>=3:
                    result[person] = record[ idx: i]
                    break
    print(result)

badge2(test2)








    #     #################
    # enterw = set()
    # exitw = set()
    # # list based on time sequence
    # count = defaultdict(int)
    # for item in entrylist:
    #     person = item[0]
    #     action = item[1]
    #     prev = count.get(person)
    #     if action == "enter":
    #         if prev and prev != 0:
    #             exitw.add(person)
    #         count[person] = 1
    #     elif action == "exit":
    #         if not prev or prev!= 1:
    #             enterw.add(person)
    #         count[person] = 0
    # for k,v in count.items():
    #     if v == 1:
    #         exitw.add(k)
    # print("enter without badge:", list(enterw))
    # print("exit without badge:", list(exitw))
    #

badge1(test1)


"""

enter without badge: {'Martha'}
exit without badge: {'Paul', 'Curtis'}
{'Martha'}
{'Paul', 'Curtis'}
{'Paul': [1315, 1355, 1405], 'John': [830, 835, 855, 915, 930]}
"""