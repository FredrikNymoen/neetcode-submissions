class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        self.followMap[userId].add(userId)

        for followId in self.followMap[userId]:
            if followId in self.tweetMap:
                idx = len(self.tweetMap[followId]) - 1
                cnt, tweetId = self.tweetMap[followId][idx]
                heapq.heappush(minHeap, [cnt, tweetId, followId, idx])
        
        while minHeap and len(res) < 10:
            cnt, tweetId, followId, idx = heapq.heappop(minHeap)
            res.append(tweetId)

            if (idx - 1) >= 0:
                cnt, tweetId = self.tweetMap[followId][idx - 1]
                heapq.heappush(minHeap, [cnt, tweetId, followId, idx - 1])
        
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)
