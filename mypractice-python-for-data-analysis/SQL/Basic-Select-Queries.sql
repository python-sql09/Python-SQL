-- Basic SQL:
-- ----------
-- SELECT * FROM my_sql_works.EmployeeDemographics;

-- SELECT FirstName FROM my_sql_works.EmployeeDemographics;

-- SELECT FirstName, LastName FROM my_sql_works.EmployeeDemographics;

-- SELECT * FROM my_sql_works.EmployeeDemographics Limit 5;

-- Bottom 5 rows
/* SELECT * FROM my_sql_works.EmployeeDemographics
ORDER BY EmployeeID DESC
LIMIT 5; */

-- Bottom 5 rows
/*SELECT * FROM (
    SELECT * FROM my_sql_works.EmployeeDemographics
    ORDER BY EmployeeID DESC
    LIMIT 5
) AS subquery
ORDER BY EmployeeID ASC;*/

-- SELECT distinct(EmployeeID) FROM my_sql_works.EmployeeDemographics;

-- SELECT distinct(Gender) FROM my_sql_works.EmployeeDemographics;

-- SELECT COUNT(LastName) FROM my_sql_works.EmployeeDemographics;

-- SELECT COUNT(LastName) AS LastNameCount FROM my_sql_works.EmployeeDemographics;

-- SELECT * FROM my_sql_works.EmployeeSalary;

-- SELECT max(Salary) FROM my_sql_works.EmployeeSalary;

-- SELECT AVG(Salary) FROM my_sql_works.EmployeeSalary;

-- SELECT max(Salary) FROM my_sql_works.EmployeeSalary;

-- Where:
 
/* SELECT * FROM my_sql_works.EmployeeDemographics 
where FirstName <> 'Jim';*/

/* SELECT * FROM my_sql_works.EmployeeDemographics 
where Age > 30 ;

SELECT * FROM my_sql_works.EmployeeDemographics 
where Age >= 30 ; 

SELECT * FROM my_sql_works.EmployeeDemographics 
where Age < 32 ; 

SELECT * FROM my_sql_works.EmployeeDemographics 
where Age <= 32 AND Gender = 'Male'; 

SELECT * FROM my_sql_works.EmployeeDemographics 
where Age <= 32 OR Gender = 'Male'; 

-- Like:
SELECT * FROM my_sql_works.EmployeeDemographics 
where LastName Like 'S%'; 

SELECT * FROM my_sql_works.EmployeeDemographics 
where LastName Like '%S%'; 

SELECT * FROM my_sql_works.EmployeeDemographics 
where LastName Like 'S%o%'; 

SELECT * FROM my_sql_works.EmployeeDemographics 
where LastName Like 'S%c%ott%'; 

-- Null, Not Null
SELECT * FROM my_sql_works.EmployeeDemographics 
where FirstName is NULL; 

SELECT * FROM my_sql_works.EmployeeDemographics 
where FirstName is NOT NULL; 

-- IN
SELECT * FROM my_sql_works.EmployeeDemographics 
where FirstName IN ('Jim', 'Michael', 'kevin'); */

/* Group By, Order By */
/*-------------------*/
-- SELECT DISTINCT(Gender) FROM my_sql_works.EmployeeDemographics; 

/* SELECT Gender FROM my_sql_works.EmployeeDemographics
GROUP BY Gender; 

SELECT Gender, COUNT(Gender) FROM my_sql_works.EmployeeDemographics
GROUP BY Gender; */

-- SELECT * FROM my_sql_works.EmployeeDemographics;

/* SELECT Gender, Age, COUNT(Gender) FROM my_sql_works.EmployeeDemographics
GROUP BY Gender, Age; 

SELECT Gender, COUNT(Gender) FROM my_sql_works.EmployeeDemographics
GROUP BY Gender; 

SELECT Gender, COUNT(Gender) FROM my_sql_works.EmployeeDemographics
WHERE Age > 31
GROUP BY Gender; 

SELECT Gender, COUNT(Gender) AS CountGender
FROM my_sql_works.EmployeeDemographics
WHERE Age > 31
GROUP BY Gender
ORDER BY CountGender ASC; 

SELECT Gender, COUNT(Gender) AS CountGender
FROM my_sql_works.EmployeeDemographics
WHERE Age > 31
GROUP BY Gender
ORDER BY CountGender DESC;

SELECT Gender, COUNT(Gender) AS CountGender
FROM my_sql_works.EmployeeDemographics
WHERE Age > 31
GROUP BY Gender
ORDER BY CountGender ASC; 

SELECT Gender, COUNT(Gender) AS CountGender
FROM my_sql_works.EmployeeDemographics
WHERE Age > 31
GROUP BY Gender
ORDER BY Gender DESC;

SELECT Gender, COUNT(Gender) AS CountGender
FROM my_sql_works.EmployeeDemographics
WHERE Age > 31
GROUP BY Gender
ORDER BY Gender ASC;  

select * from my_sql_works.EmployeeDemographics
order by age 

select * from my_sql_works.EmployeeDemographics
order by age DESC; 

select * from my_sql_works.EmployeeDemographics
order by age, Gender;

select * from my_sql_works.EmployeeDemographics
order by age, Gender DESC; 

select * from my_sql_works.EmployeeDemographics
order by age DESC, Gender DESC; 

select * from my_sql_works.EmployeeDemographics
order by 4 Desc, 5 Desc */
