class Twitter:

    def __init__(self):
        # Time&Space O(1)
        self.tweet_num = 0
        self.posts = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Time O(1) & Space O(1)
        self.posts[userId].append((self.tweet_num, tweetId))
        self.tweet_num += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # Time O(len(followees)) & Space O(len(followees))
        followees = list(self.following[userId])
        followees.append(userId)

        pointers = {f:len(self.posts[f])-1 for f in followees}

        res = []
        for i in range(10):
            latest_tweet = (float("-inf"), -1, 0)
            for f in followees:
                if pointers[f] < 0: continue
                this_tweet = self.posts[f][pointers[f]] 
                if this_tweet[0] > latest_tweet[0]:
                    latest_tweet = (*this_tweet, f)

            if latest_tweet[1] >= 0:
                res.append(latest_tweet[1])
                pointers[latest_tweet[2]] -= 1

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        # Time&Space O(1)
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Time&Space O(1)
        self.following[followerId].discard(followeeId)