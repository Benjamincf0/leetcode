class Twitter:

    def __init__(self):
        self.tweet_num = 0
        self.posts = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((self.tweet_num, tweetId))
        # if len(self.posts[userId]) > 10:
        #     # remove oldest
        #     self.posts[userId].popleft()
        self.tweet_num += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # print(self.posts)
        # print(self.following)
        followees = list(self.following[userId])
        followees.append(userId)

        pointers = {f:len(self.posts[f])-1 for f in followees}

        res = []
        for i in range(10):
            min_tweet = (float("-inf"), -1, 0)
            for f in followees:
                if pointers[f] < 0: continue
                this_tweet = self.posts[f][pointers[f]] 
                if this_tweet[0] > min_tweet[0]:
                    min_tweet = (*this_tweet, f)

            if min_tweet[1] >= 0:
                res.append(min_tweet[1])
                # print(min_tweet)
                pointers[min_tweet[2]] -= 1

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)