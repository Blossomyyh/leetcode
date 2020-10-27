
"""
dictionary remember already dropped element
3 sections for gates
    check > required(i, i-k)
        if dic[sec] != i:(have not drop by other gates)
            dic[sec] = i
            drop +=1
input: list of requestTime
output: dropnum

3 window
1s, 3
10s, 20
60s, 60

"""


def throttlingGateway(request):
    drop = 0
    alreadyDrop = {}
    for i, req in enumerate(request):
        if i>=3 and req==request[i-3]:
            # first gate
            if req not in alreadyDrop or alreadyDrop[req]!=i:
                alreadyDrop[req] = i
                drop+=1

        '''the interval between 2 reqtime is less than 10 --> need drop'''
        if i >= 20 and req - request[i - 20]<10:
            # first gate
            if req not in alreadyDrop or alreadyDrop[req] != i:
                alreadyDrop[req] = i
                drop += 1

        if i >=60 and req - request[i - 60]<60:
            # first gate
            if req not in alreadyDrop or alreadyDrop[req] != i:
                alreadyDrop[req] = i
                drop += 1
    return drop



# (Time complexity: O(n))

def droppedRequest(requestTime):

    dropped = 0
	# this is to keep track of any of the element that is already dropped due to any of 3 limit violation.
    already_dropped = {}

    for i in range(len(requestTime)):
        if i > 2 and requestTime[i] == requestTime[i-3]:
            if requestTime[i] not in already_dropped or already_dropped[requestTime[i]] != i:
                already_dropped[requestTime[i]] = i
                dropped += 1
                print(i, requestTime[i])

        elif i > 19 and requestTime[i] - requestTime[i-20] < 10:
            if requestTime[i] not in already_dropped or already_dropped[requestTime[i]] != i:
                already_dropped[requestTime[i]] = i
                dropped += 1
                print(i, requestTime[i])

        elif i > 59 and requestTime[i] - requestTime[i-60] < 60:
            if requestTime[i] not in already_dropped or already_dropped[requestTime[i]] != i:
                already_dropped[requestTime[i]] = i
                dropped += 1
                print(i, requestTime[i])

    return dropped


"""
The gateway has the following limits:
The number of transactions in any given second cannot exceed 3.
The number of transactions in any given 10 second period cannot exceed 20. A ten-second period includes all requests arriving from any time max(1, T-9) to T (inclusive of both) for any valid time T.
The number of transactions in any given minute cannot exceed 60. Similar to above, 1 minute is from max(1, T-59) to T.
Any request that exceeds any of the above limits will be dropped by the gateway. Given the times at which different requests arrive sorted ascending, find how many requests will be dropped.
Note: Even if a request is dropped it is still considered for future calculations. Although, if a request is to be dropped due to multiple violations, it is still counted only once.
Example
n = 27
requestTime = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 11, 11, 11, 11 ]
Request 1 - Not Dropped.
Request 1 - Not Dropped.
Request 1 - Not Dropped.
Request 1 - Dropped. At most 3 requests are allowed in one second.
No request will be dropped till 6 as all comes at an allowed rate of 3 requests per second and the 10-second clause is also not violated.
Request 7 - Not Dropped. The total number of requests has reached 20 now.
Request 7 - Dropped. At most 20 requests are allowed in ten seconds.
Request 7 - Dropped. At most 20 requests are allowed in ten seconds.
Request 7 - Dropped. At most 20 requests are allowed in ten seconds. Note that the 1-second limit is also violated here.
Request 11 - Not Dropped. The 10-second window has now become 2 to 11. Hence the total number of requests in this window is 20 now.
Request 11 - Dropped. At most 20 requests are allowed in ten seconds.
Request 11 - Dropped. At most 20 requests are allowed in ten seconds.
Request 11 - Dropped. At most 20 requests are allowed in ten seconds. Also, at most 3 requests are allowed per second.
Hence, a total of 7 requests are dropped.
Function Description
Complete the droppedRequests function in the editor below.
droppedRequests has the following parameter(s):
int requestTime[n]: an ordered array of integers that represent the times of various requests
Returns
int: the total number of dropped requests
Constraints
1 ≤ n ≤ 106
1 ≤ requestTime[i] ≤ 109
Input Format For Custom Testing
Sample Case 0
Sample Input For Custom Testing
STDIN Function
----- --------
5 → requestTime[] size n = 5
1 → requestTime = [ 1, 1, 1, 1, 2 ]
1
1
1
2
Sample Output
1
Explanation
There are 4 requests that arrive at second 1. This exceeds the per second limit so one packet is dropped. No other limits are exceeded.```
"""