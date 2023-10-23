"""
https://leetcode.com/problems/article-views-i/description
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| article_id    | int     |
| author_id     | int     |
| viewer_id     | int     |
| view_date     | date    |
+---------------+---------+
There is no primary key (column with unique values) for this table, the table may have duplicate rows.
Each row of this table indicates that some viewer viewed an article (written by some author) on some date. 
Note that equal author_id and viewer_id indicate the same person.
 

Write a solution to find all the authors that viewed at least one of their own articles.

Return the result table sorted by id in ascending order.

The result format is in the following example.

 

Example 1:

Input: 
Views table:
+------------+-----------+-----------+------------+
| article_id | author_id | viewer_id | view_date  |
+------------+-----------+-----------+------------+
| 1          | 3         | 5         | 2019-08-01 |
| 1          | 3         | 6         | 2019-08-02 |
| 2          | 7         | 7         | 2019-08-01 |
| 2          | 7         | 6         | 2019-08-02 |
| 4          | 7         | 1         | 2019-07-22 |
| 3          | 4         | 4         | 2019-07-21 |
| 3          | 4         | 4         | 2019-07-21 |
+------------+-----------+-----------+------------+
Output: 
+------+
| id   |
+------+
| 4    |
| 7    |
+------+

"""
data = [[1, 3, 5, '2019-08-01'], [1, 3, 6, '2019-08-02'], [2, 7, 7, '2019-08-01'], [2, 7, 6, '2019-08-02'], [4, 7, 1, '2019-07-22'], [3, 4, 4, '2019-07-21'], [3, 4, 4, '2019-07-21']]
views = pd.DataFrame(data, columns=['article_id', 'author_id', 'viewer_id', 'view_date']).astype({'article_id':'Int64', 'author_id':'Int64', 'viewer_id':'Int64', 'view_date':'datetime64[ns]'})


# solution 1 STARTS


# Filter 

import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    # Solution 1 using filter
    filtered_view = views[views['viewer_id']==views['author_id']]
    # remove duplicates
    filtered_view.drop_duplicates(subset=['author_id'], inplace=True)
    # sort_values
    filtered_view.sort_values(by='author_id', inplace=True)
    # rename columns
    filtered_view.rename(columns={'author_id':'id'}, inplace=True)
    return filtered_view[['id']]

# solution 1 ENDS

# join solution
def article_views2(views: pd.DataFrame) -> pd.DataFrame:
    views2 = views.copy()

    merge_df = views.merge(views2, how="inner", left_on=["author_id","article_id"], right_on=["viewer_id","article_id"])
    author_ids = merge_df[['author_id_x']].rename(columns={'author_id_x':'id'})
    unique_author_ids = author_ids.drop_duplicates().reset_index()[['id']]
    return unique_author_ids.sort_values('id')
