import heapq
from typing import List

"""
Method 1: post efficient
add post in constant time & build a heap while getting news feed. (slightly inefficient than method 2)
"""


class Twitter:

    def __init__(self):
        """
        Method: add newly added post against author & followers.
        """
        self.nonce = 0
        self.follows = {}
        self.user_post = {}

    def get_nonce(self):
        self.nonce -= 1
        return self.nonce

    def get_or_create_follows(self, user_id):
        self.follows[user_id] = self.follows.get(user_id, {user_id})
        return self.follows[user_id]

    def get_user_posts(self, user_id):
        self.user_post[user_id] = self.user_post.get(user_id, [])
        return self.user_post[user_id]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.get_user_posts(userId).append((self.get_nonce(), tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []

        for f in self.get_or_create_follows(userId):
            user_posts = self.get_user_posts(f)
            if user_posts:
                heapq.heappush(heap, (*user_posts[len(user_posts) - 1], len(user_posts) - 1, f))

        n = 10
        res = []
        while n and heap:
            _, post, idx, f = heapq.heappop(heap)
            res.append(post)
            user_posts = self.get_user_posts(f)
            if idx - 1 >= 0:
                heapq.heappush(heap, (*user_posts[idx - 1], idx - 1, f))

            n -= 1

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.get_or_create_follows(followerId).add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.get_or_create_follows(followerId):
            self.get_or_create_follows(followerId).remove(followeeId)


"""
Method 2: add newly added post against author & followers in form of a heap.
Retrieve news feeds directly from constructed heap. 
class Twitter:

    def __init__(self):
        self.followers = {}
        self.following = {}
        self.user_post = {}
        self.__nonce__ = 0

    def __get_nonce__(self):
        self.__nonce__ -= 1
        return self.__nonce__

    def __add_tweet__(self, author, user_id, tweet_id):
        self.user_post[user_id] = self.user_post.get(user_id, [])
        heapq.heappush(self.user_post[user_id], (self.__get_nonce__(), author, tweet_id))

    def postTweet(self, userId: int, tweetId: int) -> None:
        followers = self.followers.get(userId, set())
        self.__add_tweet__(userId, userId, tweetId)
        for follower in followers:
            self.__add_tweet__(userId, follower, tweetId)

    def getNewsFeed(self, userId: int) -> List[int]:
        following = self.following.get(userId, set())
        n = 10
        res = []
        while self.user_post.get(userId, []) and n:
            nonce, author, tweet_id = heapq.heappop(self.user_post[userId])
            if author == userId or author in following:
                if not res or res[-1][2] != tweet_id:
                    res.append((nonce, author, tweet_id))
                    n -= 1

        for nonce, author, tweet_id in res:
            heapq.heappush(self.user_post[userId], (nonce, author, tweet_id))

        return [tweet_id for _, _, tweet_id in res]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followeeId] = self.followers.get(followeeId, set())
        self.followers[followeeId].add(followerId)
        self.following[followerId] = self.following.get(followerId, set())
        self.following[followerId].add(followeeId)

        self.user_post[followeeId] = self.user_post.get(followeeId, [])
        self.user_post[followerId] = self.user_post.get(followerId, [])
        for n, a, t in self.user_post[followeeId]:
            heapq.heappush(self.user_post[followerId], (n, a, t))

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following.get(followerId, set()):
            self.following[followerId].remove(followeeId)

        if followerId in self.followers.get(followeeId, set()):
            self.followers[followeeId].remove(followerId)
"""

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
