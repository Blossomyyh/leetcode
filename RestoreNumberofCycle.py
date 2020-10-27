"""
Restore numbers on circle
Given a list:
 a,b — a and b is friends
[[a, b],[a, c],[c, d],[e, f], [f, g],[f, e],[g, h], [h,b],[h, g]]
Now they are going to have dinner together, but everyone wants to seat with their friends
Like:
        a
    c       b
d              h
   e           g
        f
Output: A sequence to arrange them properly (can start from any one)
like  [c, d, e, f, g, h, b, a] or [g, h, b, a, c, d, e, f]
"""

'''
\\ 1.create dictionary for relations
\\ 2.set up visited and person set, start from any point
\\ 3. do dfs, cur person, cur list:
    if len== all: return list
    
    for one in friends:
       if not in visited:
            append and do dfs and return
    else we need to search for the rest of the people to 
    for p in people but not in visited:
         append and do dfs and return


'''

from collections import defaultdict

friends = [['a', 'b'],['a', 'c'],['c', 'd'],['e', 'f'],['f', 'g'],['f', 'e'],['g', 'h'],['h','b'],['h', 'g']]


def findCircle(friends):

    # dictionary to store relationships
    relation = defaultdict(set)
    people = set()
    for a, b in friends:
        people.add(a)
        people.add(b)
        relation[a].add(b)
        relation[b].add(a)
    visited = set()

    def dfs(person, curlist):
        visited.add(person)
        print(person, curlist)
        if len(curlist) == len(people):

            return curlist
        for i in relation[person]:
            if i not in visited:
                return dfs(i, curlist +[i])
        for p in people:
            if p not in visited:
                return dfs(p, curlist + [p])


    return dfs('a', ['a'])

findCircle(friends)




person = set()
d = defaultdict(set)
start = None

for x, y in friends:
  person.add(x)
  person.add(y)
  d[x].add(y)
  d[y].add(x)
  start = x

print(d)
ans = []

def dfs(cur, record):
  print(cur, record)
  if len(record) == len(person):
    if (d[cur] and record[0] in d[cur]) or not d[cur]:
      # ans.append(record)
      return record
  if d[cur]:
    for t in d[cur]:
      if t not in record:
        return dfs(t, record + [t])
  for p in person:
    if p not in record:
      return dfs(p, record + [p])

dfs(start, [start])
# print(ans)



dic = {1:2}
dic.pop(1)
print(dic)