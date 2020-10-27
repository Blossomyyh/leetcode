"""
stale jobs ($0-noe, $1-pretask)

topological sort

################################
1. given a list sort by requirements
create a dic : key the prerequest, value list - following jobs
and indegree(job's pre number) dictionary

queue = []
res = []
add all job which indegree==0 into the queue
while queue:
    node = pop()
    res.append node
    for following in dic[node]:
        ingree[following] --
        if in ==0:
            queue.append
return res
###############################

2. have exe time for each job
PICK OUT NOT QUALIFIED ONES
need another parent to node dictionary
for each node in iteration:
    if p already in set():
        add this child --> sequence not right
    check whether its node's time all < p'time
    else
        add this child



"""

preTasks = [
    ["clean", "mapper"],
    ["metadata", "statistics"],
    ["mapper", "update"],
    ["update", "statistics"],
    ["clean", "metadata"],
    ["mapper", "reducer"],
    ["metadata", "timestamp"]
]

exec_times = {
    "clean": "20170302-1129",
    "mapper": "20170302-1155",
    "update": "20170302-1150",
    "statistics": "20170302-1153",
    "metadata": "20170302-1130",
    "reducer": "20170302-1540"
}
#  {'clean': ['mapper', 'metadata'], 'mapper': ['update', 'reducer'], 'metadata': ['timestamp'], 'statistics': [], 'update': ['statistics'], 'reducer': [], 'timestamp': []})
#  {'clean': 0, 'mapper': 1, 'metadata': 1, 'statistics': 2, 'update': 1, 'reducer': 1, 'timestamp': 1})

from collections import defaultdict
from collections import deque
def stalejob(preTask, times):
    parentToNode = defaultdict(list)
    nodeToParent = defaultdict(list)
    indegree = defaultdict(int)
    for pres, task in preTask:
        parentToNode[task].append(pres)
        if pres not in parentToNode :
            parentToNode[pres] = []
        """indegree means how many times ele serve as parent/referred"""
        if pres not in indegree:
            indegree[pres] = 0
        indegree[task] = indegree.get(task, 0) + 1
        nodeToParent[pres].append(task)
        if task not in nodeToParent:
            nodeToParent[task] = []

    print(parentToNode)
    print(indegree)

    queue = deque()
    res = []

    result = set()

    for node in indegree:
        if indegree[node] ==0:
            queue.append(node)
    while queue:
        node = queue.popleft()
        # get the time of it from exetime
        lasttime = exec_times.get(node, "0")
        res.append(node)

        # make sure child is done before parent!
        for p in parentToNode[node]:
            if (p in result) or lasttime < exec_times[p]:
                result.add(node)


        """ \\ !!! Topological use child to parent and parent's indegree to sort!!! """
        for p in nodeToParent[node]:
            indegree[p] -=1
            if indegree[p]==0:
                queue.append(p)
    print(result)
    return res
print(stalejob(preTasks, exec_times))


