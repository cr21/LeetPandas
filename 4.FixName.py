"""
https://leetcode.com/problems/fix-names-in-a-table/
1667. Fix Names in a Table
+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| user_id        | int     |
| name           | varchar |
+----------------+---------+
user_id is the primary key (column with unique values) for this table.
This table contains the ID and the name of the user. The name consists of only lowercase and uppercase characters.
 

Write a solution to fix the names so that only the first character is uppercase and the rest are lowercase.

Return the result table ordered by user_id.

The result format is in the following example.

 

Example 1:

Input: 
Users table:
+---------+-------+
| user_id | name  |
+---------+-------+
| 1       | aLice |
| 2       | bOB   |
+---------+-------+
Output: 
+---------+-------+
| user_id | name  |
+---------+-------+
| 1       | Alice |
| 2       | Bob   |
+---------+-------+

category : apply
"""

data = [[1, 'aLice'], [2, 'bOB']]
users = pd.DataFrame(data, columns=['user_id', 'name']).astype({'user_id':'Int64', 'name':'object'})



import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:

    def update_name(user):
        return user['name'][0].upper() + user['name'][1:].lower()
    users['name']=users.apply(update_name, axis=1)
    return users.sort_values('user_id')
