import tweepy
from decouple import config

# Authenticate with the Twitter API using environment variables
consumer_key = config('TWITTER_CONSUMER_KEY')
consumer_secret = config('TWITTER_CONSUMER_SECRET')
access_token = config('TWITTER_ACCESS_TOKEN')
access_token_secret = config('TWITTER_ACCESS_TOKEN_SECRET')

# Authenticate with the Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Define a function to post a tweet
def post_tweet(tweet_text):
    try:
        api.update_status(tweet_text)
        print("Tweet posted successfully.")
    except tweepy.errors.TweepyException as e:
        print(f"Error posting tweet: {e}")

# Define a function to post a tweet with media
def post_tweet_with_media(tweet_text, media_path):
    try:
        # Upload the media
        media = api.media_upload(media_path)

        # Post the tweet with the media
        api.update_status(status=tweet_text, media_ids=[media.media_id])
        print("Tweet with media posted successfully.")
    except tweepy.errors.TweepyException as e:
        print(f"Error posting tweet with media: {e}")

# Define a function to like a tweet by tweet ID
def like_tweet(tweet_id):
    try:
        api.create_favorite(id=tweet_id)
        print("Tweet liked successfully.")
    except tweepy.errors.TweepyException as e:
        print(f"Error liking tweet: {e}")

# Define a function to look up user(s) by username
def lookup_users(usernames):
    try:
        users = api.lookup_users(screen_names=usernames)
        for user in users:
            print(f"User: @{user.screen_name}, Name: {user.name}, Followers: {user.followers_count}")
    except tweepy.errors.TweepyException as e:
        print(f"Error looking up user(s): {e}")

# Define a function to follow a user by username
def follow_user(username):
    try:
        api.create_friendship(screen_name=username)
        print(f"Followed user: @{username}")
    except tweepy.errors.TweepyException as e:
        print(f"Error following user: {e}")

if __name__ == "__main__":
#Here are some examples of how to use the functions:

    tweet_text = "Hello, Twitter! This is a test tweet."
    post_tweet(tweet_text)

    media_path = 'media/path.jpg'  # Replace with the actual path to your image file
    post_tweet_with_media("Check out this cool image!", media_path)

    tweet_id_to_like = 'TWEET_ID_TO_LIKE'
    like_tweet(tweet_id_to_like)

    usernames_to_lookup = ['user1', 'user2']  # Replace with the usernames you want to look up
    lookup_users(usernames_to_lookup)

    username_to_follow = 'user_to_follow'  # Replace with the username you want to follow
    follow_user(username_to_follow)