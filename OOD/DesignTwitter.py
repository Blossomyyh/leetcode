from collections import defaultdict
import heapq
from typing import List

class Twitter:
    def __init__(self):
        """"""
        """
        Initialize your data structure here.
        \\\\\\ order is negative --> get most recent in heap
        """
        self.followees = defaultdict(set)
        self.tweets = defaultdict(list)
        self.order = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        need --order
        """
        self.tweets[userId].append((self.order, tweetId))
        self.order -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        """"""
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        \\\\ user can follow himself  [in xx[id] | set([userId])]

        \\\\ whether key in dic

        \\\\ heap to get most recent 10
        """
        ts = []
        # print(self.tweets)

        if userId in self.followees:
            hashset = self.followees[userId]
            for f in hashset | set([userId]):
                if f in self.tweets:
                    ts.extend(self.tweets[f])
        else:
            if userId in self.tweets:
                ts.extend(self.tweets[userId])
        c = 10
        res = []

        heapq.heapify(ts)
        while ts and c:
            res.append(heapq.heappop(ts)[1])
            c -= 1

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """"""
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        \\\\\\ check key exist
        """

        if followeeId in self.followees[followerId]:
            self.followees[followerId].remove(followeeId)


"""
Twitter twitter = new Twitter();

// User 1 posts a new tweet (id = 5).
twitter.postTweet(1, 5);

// User 1's news feed should return a list with 1 tweet id -> [5].
twitter.getNewsFeed(1);

// User 1 follows user 2.
twitter.follow(1, 2);

// User 2 posts a new tweet (id = 6).
twitter.postTweet(2, 6);

// User 1's news feed should return a list with 2 tweet ids -> [6, 5].
// Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.getNewsFeed(1);

// User 1 unfollows user 2.
twitter.unfollow(1, 2);

// User 1's news feed should return a list with 1 tweet id -> [5],
// since user 1 is no longer following user 2.
twitter.getNewsFeed(1);
"""