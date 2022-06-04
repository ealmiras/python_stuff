tweet = input("Type your tweet here: ")
tweet_len = len(tweet)

max_chars = 140

if tweet_len <= max_chars:
    print(f"Your {tweet_len} char tweet will work!")
else:
    print(f"Your {tweet_len} char tweet is {tweet_len - max_chars} char longer than {max_chars} char")

