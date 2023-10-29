"""

178. Rank Scores
https://leetcode.com/problems/rank-scores/description
/rank_scores.py
Write a solution to find the rank of the scores. The ranking should be calculated according to the following rules:

The scores should be ranked from the highest to the lowest.
If there is a tie between two scores, both should have the same ranking.
After a tie, the next ranking number should be the next consecutive integer value. In other words, there should be no holes between ranks.
Return the result table ordered by score in descending order.

====================================================================================================================================================================================

Table: Scores

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| score       | decimal |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table contains the score of a game. Score is a floating point value with two decimal places.
 

Write a solution to find the rank of the scores. The ranking should be calculated according to the following rules:

The scores should be ranked from the highest to the lowest.
If there is a tie between two scores, both should have the same ranking.
After a tie, the next ranking number should be the next consecutive integer value. In other words, there should be no holes between ranks.
Return the result table ordered by score in descending order.

The result format is in the following example.

 

Example 1:

Input: 
Scores table:
+----+-------+
| id | score |
+----+-------+
| 1  | 3.50  |
| 2  | 3.65  |
| 3  | 4.00  |
| 4  | 3.85  |
| 5  | 4.00  |
| 6  | 3.65  |
+----+-------+
Output: 
+-------+------+
| score | rank |
+-------+------+
| 4.00  | 1    |
| 4.00  | 1    |
| 3.85  | 2    |
| 3.65  | 3    |
| 3.65  | 3    |
| 3.50  | 4    |
+-------+------+
"""
import pandas as pd
data = [[1, 3.5], [2, 3.65], [3, 4.0], [4, 3.85], [5, 4.0], [6, 3.65]]
scores = pd.DataFrame(data, columns=['id', 'score']).astype({'id':'Int64', 'score':'Float64'})


def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    # solution 1 
    # rank functions
    scores['rank'] = scores['score'].rank(method='dense', ascending=False)

    return scores[['score','rank']].sort_values('score', ascending=False)

    # Solution 2
    # creative solution using join
    unique_scores = scores[['score']]\
                    .drop_duplicates()\
                    .sort_values(by='score',ascending=False)
                    # .reset_index()[['score']]
    unique_scores['rank']=[i+1 for i in range(len(unique_scores))]
    df = scores\
            .merge(unique_scores, on='score', how='inner')\
            .sort_values(by='score', ascending=False)

    return df[['score','rank']]

