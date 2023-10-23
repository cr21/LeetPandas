"""
Write a solution to find the IDs of the invalid tweets. The tweet is invalid if the number of characters used in the content of the tweet is strictly greater than 15.

Return the result table in any order.
+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| tweet_id       | int     |
| content        | varchar |
+----------------+---------+
tweet_id is the primary key (column with unique values) for this table.
This table contains all the tweets in a social media app.

Example 1:

Input: 
Tweets table:
+----------+----------------------------------+
| tweet_id | content                          |
+----------+----------------------------------+
| 1        | Vote for Biden                   |
| 2        | Let us make America great again! |
+----------+----------------------------------+
Output: 
+----------+
| tweet_id |
+----------+
| 2        |
+----------+
Explanation: 
Tweet 1 has length = 14. It is a valid tweet.
Tweet 2 has length = 32. It is an invalid tweet.

Category : Filters
Difficulty : Easy

"""


data = [[1, 'Vote for Biden'], [2, 'Let us make America great again!']]
tweets = pd.DataFrame(data, columns=['tweet_id', 'content']).astype({'tweet_id':'Int64', 'content':'object'})

import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    # approach 1 apply function
    length_check_mask = tweets['content'].apply(lambda twit:  len(twit)>15)

    # approach 2 using string length function
    length_check_mask = tweets['content'].str.len() > 15
    return tweets[length_check_mask][['tweet_id']]
