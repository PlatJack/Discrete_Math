import snscrape.modules.twitter as sntwitter
import pandas as pd

# Creating list to append tweet data to
attributes_container = []

# Using TwitterSearchScraper to scrape data and append tweets to list
for i, tweet in enumerate(sntwitter.TwitterSearchScraper('DOGECOIN since:2021-12-31 until:2022-12-05').get_items()):
    if i > 10000:
        break
    attributes_container.append(
        [tweet.user.username, tweet.date, tweet.likeCount, tweet.sourceLabel, tweet.content])

# Creating a dataframe to load the list
tweets_df = pd.DataFrame(attributes_container, columns=[
                         "User", "Date Created", "Number of Likes", "Source of Tweet", "Tweet"])
tweets_df.to_csv('tweets_DOGE.csv')
