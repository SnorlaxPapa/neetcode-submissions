import heapq
class Twitter:
    """
    design Twitter.
    Initital thought: we need a global time tracker to track the time of posts
    We initialize a hash map for each user with k:v pair user: (following, own_posts)
    own_posts is a list with their own posts 
    Following is a set

    For postTweet, every time a tweet is posted, we add to map[user][1] with (time, tweetId) in O(1) time
    For follow, we add the user to the following set in O(1) time
    For unfollow, we del the user from the set in O(1) time

    For getNewsFeed, 
    We allocate a min heap newsFeed that we maintain at size 10

    We iterate through the following set, taking 10 posts each from each person we're following 
    Each step. We add to the min heap. If its size is 10, we heappop the root which is the least recent post
    This operation will be O(10 * followers + posts) in time, O(10) in space which is fundamentally O(F) and O(1)
    """
    def __init__(self):
        self.users = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        #add tweet to user hashmap. initialize if it doesn't exist
        new_tweet = (self.time, tweetId)

        if userId not in self.users: 
            self.users[userId] = (set(), [])
        self.users[userId][1].append(new_tweet) 

        self.time += 1


    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.users: return []

        news_feed = []
        followees = self.users[userId][0]
        followees.add(userId)
        for followee in followees:
            if followee not in self.users: continue

            followee_tweets = self.users[followee][1][-10: ]
            for tweet in followee_tweets:
                heapq.heappush(news_feed, tweet)

                if len(news_feed) > 10:
                    heapq.heappop(news_feed)
        followees.discard(userId)

        sorted_newsfeed = sorted(news_feed, key=lambda x: x[0], reverse=True)
        return [tweet[1] for tweet in sorted_newsfeed]


    def follow(self, followerId: int, followeeId: int) -> None:
        #add followeeId to set
        if followerId not in self.users:
            self.users[followerId] = (set(), [])
        self.users[followerId][0].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users: return
        #discard followeeId from set
        follower_list = self.users[followerId][0]
        follower_list.discard(followeeId)
        
