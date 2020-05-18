from app import db



class TweetsModel(db.Model):
    __tablename__ = 'jobs'

    id = db.Column(db.Integer, primary_key=True)
    rawTweet = db.Column(db.String())
    cleanedTweet = db.Column(db.String())
    retweetCount = db.Column(db.String())
    favoriteCount = db.Column(db.String())
    isReply = db.Column(db.String())

    UserCreatedDate = db.Column(db.String())
    UserLikesNo = db.Column(db.String())
    UserFollowerNo = db.Column(db.String())
    UserFriendsNo = db.Column(db.String())
    UserListNo = db.Column(db.String())
    UserTotalTweet = db.Column(db.String())
    UserIsVerified = db.Column(db.String())
    UserLocation = db.Column(db.String())

    author = db.Column(db.String())
    hashtags = db.Column(db.String())
    urls = db.Column(db.String())
    likelyJobNames = db.Column(db.String())
    userPicture = db.Column(db.String())

    def __init__(self, rawTweet, cleanedTweet, retweetCount, favoriteCount, isReply, UserCreatedDate, UserLikesNo,
                 UserFollowerNo, UserFriendsNo, UserListNo, UserTotalTweet, UserIsVerified, UserLocation, author,
                 hashtags, urls, likelyJobNames,userPicture):
        self.rawTweet = rawTweet
        self.cleanedTweet = cleanedTweet
        self.retweetCount = retweetCount
        self.favoriteCount = favoriteCount
        self.isReply = isReply
        self.UserCreatedDate = UserCreatedDate
        self.UserLikesNo = UserLikesNo
        self.UserFollowerNo = UserFollowerNo
        self.UserFriendsNo = UserFriendsNo
        self.UserListNo = UserListNo
        self.UserTotalTweet = UserTotalTweet
        self.UserIsVerified = UserIsVerified
        self.UserLocation = UserLocation
        self.retweetCount = retweetCount
        self.author = author
        self.hashtags = hashtags
        self.urls = urls
        self.likelyJobNames = likelyJobNames
        self.userPicture = userPicture




