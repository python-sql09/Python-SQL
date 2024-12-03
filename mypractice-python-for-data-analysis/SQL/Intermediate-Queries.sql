-- Intermediate Queries:
-- ---------------------
-- Joins:
-- Inner Join
/* Select * from my_sql_works.EmployeeDemographics
Inner Join my_sql_works.EmployeeSalary
ON EmployeeDemographics.EmployeeID = EmployeeSalary.EmployeeID;
*/
-- Full Outer Join: (Not Directly work in MySQL)
/* Select * from my_sql_works.EmployeeDemographics
Full Outer Join my_sql_works.EmployeeSalary
ON EmployeeDemographics.EmployeeID = EmployeeSalary.EmployeeID;

-- Left join union Right join  = Full outer joinEmployeeDemographics1
SELECT * 
FROM my_sql_works.EmployeeDemographics AS ed
LEFT JOIN my_sql_works.EmployeeSalary AS es
ON ed.EmployeeID = es.EmployeeID
UNION
SELECT * 
FROM my_sql_works.EmployeeDemographics AS ed
RIGHT JOIN my_sql_works.EmployeeSalary AS es
ON ed.EmployeeID = es.EmployeeID;  

-- Left Outer Join:
Select * from my_sql_works.EmployeeDemographics
Left Outer Join my_sql_works.EmployeeSalary
ON EmployeeDemographics.EmployeeID = EmployeeSalary.EmployeeID; */

-- Right Outer Join:
Select * from my_sql_works.EmployeeDemographics
Right Outer Join my_sql_works.EmployeeSalary
ON EmployeeDemographics.EmployeeID = EmployeeSalary.EmployeeID;