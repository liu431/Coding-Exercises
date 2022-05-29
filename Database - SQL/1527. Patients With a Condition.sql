# Write your MySQL query statement below
# Report the patient_id, patient_name all conditions of patients who have Type I Diabetes. 
## Type I Diabetes always starts with DIAB1 prefix
## '% DIAB1%' condition as some conditions have other words in front of DIAB1
SELECT patient_id, patient_name, conditions
FROM Patients
WHERE conditions LIKE 'DIAB1%' OR conditions LIKE '% DIAB1%'
