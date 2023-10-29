"""

https://leetcode.com/problems/nth-highest-salary/description
/NthHigestSalary.py
177. Nth Highest Salary
Write a solution to find the nth highest salary from the Employee table. If there is no nth highest salary, return null.

==============================================================================================================================
Table: Employee

+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
Each row of this table contains information about the salary of an employee.
 

Write a solution to find the nth highest salary from the Employee table. If there is no nth highest salary, return null.

The result format is in the following example.

 

Example 1:

Input: 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
n = 2
Output: 
+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| 200                    |
+------------------------+
Example 2:

Input: 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
+----+--------+
n = 2
Output: 
+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| null                   |
+------------------------

"""

data = [[1, 100], [2, 200], [3, 300]]
employee = pd.DataFrame(data, columns=['Id', 'Salary']).astype({'Id':'Int64', 'Salary':'Int64'})
import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    
    df = employee[['salary']].drop_duplicates()
    if N > len(df):
        res=None
    else:
        res = df.sort_values('salary', ascending=False).iloc[N-1][0]
    
    return pd.DataFrame({f'getNthHighestSalary({N})':[res]})
    
