"""
https://leetcode.com/problems/department-highest-salary/
department_highest_salary.py
184. Department Highest Salary

able: Employee

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| id           | int     |
| name         | varchar |
| salary       | int     |
| departmentId | int     |
+--------------+---------+
id is the primary key (column with unique values) for this table.
departmentId is a foreign key (reference columns) of the ID from the Department table.
Each row of this table indicates the ID, name, and salary of an employee. It also contains the ID of their department.
 

Table: Department

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table. It is guaranteed that department name is not NULL.
Each row of this table indicates the ID of a department and its name.
 

Write a solution to find employees who have the highest salary in each of the departments.

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Employee table:
+----+-------+--------+--------------+
| id | name  | salary | departmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 70000  | 1            |
| 2  | Jim   | 90000  | 1            |
| 3  | Henry | 80000  | 2            |
| 4  | Sam   | 60000  | 2            |
| 5  | Max   | 90000  | 1            |
+----+-------+--------+--------------+
Department table:
+----+-------+
| id | name  |
+----+-------+
| 1  | IT    |
| 2  | Sales |
+----+-------+
Output: 
+------------+----------+--------+
| Department | Employee | Salary |
+------------+----------+--------+
| IT         | Jim      | 90000  |
| Sales      | Henry    | 80000  |
| IT         | Max      | 90000  |
+------------+----------+--------+
Explanation: Max and Jim both have the highest salary in the IT department and Henry has the highest salary in the Sales department.

"""

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import pandas as pd
data = [[1, 'Joe', 70000, 1], [2, 'Jim', 90000, 1], [3, 'Henry', 80000, 2], [4, 'Sam', 60000, 2], [5, 'Max', 90000, 1]]
employee = pd.DataFrame(data, columns=['id', 'name', 'salary', 'departmentId']).astype({'id':'Int64', 'name':'object', 'salary':'Int64', 'departmentId':'Int64'})
data = [[1, 'IT'], [2, 'Sales']]
department = pd.DataFrame(data, columns=['id', 'name']).astype({'id':'Int64', 'name':'object'})



def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:

    # Solution 1
    df = employee.merge(department, how='left',left_on='departmentId', right_on='id')
    df.rename(columns={'name_x':'Employee','name_y':'Department','salary':'Salary'}, inplace=True)

    dept_max = df.groupby('Department')['Salary'].transform('max')

    final_df = df[df['Salary']==dept_max]

    return final_df[['Department','Salary','Employee']]
    # Solution 2
    dept_wise_max = employee[['departmentId','salary']]\
                                    .groupby('departmentId')\
                                    .agg('max')
    
    dept_emp = employee.merge(dept_wise_max, how='inner',on=['departmentId','salary'])
    final_df = dept_emp.merge(department, how='inner',left_on='departmentId', right_on='id')
    
    final_df=final_df.rename(columns={'name_x':'Employee','name_y':'Department','salary':'Salary'})
    return final_df[['Department','Employee','Salary']]
