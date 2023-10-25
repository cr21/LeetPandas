"""
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| patient_id   | int     |
| patient_name | varchar |
| conditions   | varchar |
+--------------+---------+
patient_id is the primary key (column with unique values) for this table.
'conditions' contains 0 or more code separated by spaces. 
This table contains information of the patients in the hospital.
 

Write a solution to find the patient_id, patient_name, and conditions of the patients who have Type I Diabetes. Type I Diabetes always starts with DIAB1 prefix.

Return the result table in any order.

The result format is in the following example.
1527. Patients With a Condition
https://leetcode.com/problems/patients-with-a-condition
 

Example 1:

Input: 
Patients table:
+------------+--------------+--------------+
| patient_id | patient_name | conditions   |
+------------+--------------+--------------+
| 1          | Daniel       | YFEV COUGH   |
| 2          | Alice        |              |
| 3          | Bob          | DIAB100 MYOP |
| 4          | George       | ACNE DIAB100 |
| 5          | Alain        | DIAB201      |
+------------+--------------+--------------+
Output: 
+------------+--------------+--------------+
| patient_id | patient_name | conditions   |
+------------+--------------+--------------+
| 3          | Bob          | DIAB100 MYOP |
| 4          | George       | ACNE DIAB100 | 
+------------+--------------+--------------+
Explanation: Bob and George both have a condition that starts with DIAB1.


"""

data = [[1, 'Daniel', 'YFEV COUGH'], [2, 'Alice', ''], [3, 'Bob', 'DIAB100 MYOP'], [4, 'George', 'ACNE DIAB100'], [5, 'Alain', 'DIAB201']]
patients = pd.DataFrame(data, columns=['patient_id', 'patient_name', 'conditions']).astype({'patient_id':'int64', 'patient_name':'object', 'conditions':'object'})

import pandas as pd
import re
def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    def check_diabetes_condition(patient):
        
        if patient['conditions'].startswith('DIAB1') or\
            " DIAB1" in patient['conditions']:
            return 1
        else:
            return 0
        #pattern= 'DIAB1'
        #return 1 if  pattern in patient['conditions'] else 0
        # pattern_valid = re.compile(pattern)
        # match = pattern_valid.search(patient['conditions'])
        # if match :
        #     return 1
        # else:
        #     return 0
    
    patients['Diabetes_Indicator']=patients.apply(check_diabetes_condition, axis=1)
    diabetic_patients = patients[patients['Diabetes_Indicator']==1]
    diabetic_patients.drop('Diabetes_Indicator', axis=1, inplace=True)
    return diabetic_patients
