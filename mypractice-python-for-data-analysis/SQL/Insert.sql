/* INSERT INTO my_sql_works.EmployeeDemographics
(EmployeeID,
`FirstName`,
`LastName`,
 Age,
`Gender`)
VALUES
(1001, 'Jim', 'Halpert', 30, 'Male'),
(1002, 'Pam', 'Beasley', 30, 'Female'),
(1003, 'Dwight', 'Schrute', 29, 'Male'),
(1004, 'Angela', 'Martin', 31, 'Female'),
(1005, 'Toby', 'Flenderson', 32, 'Male'),
(1006, 'Michael', 'Scott', 35, 'Male'),
(1007, 'Meredith', 'Palmer', 32, 'Female'),
(1008, 'Stanley', 'Hudson', 38, 'Male'),
(1009, 'Kevin', 'Malone', 31, 'Male');

INSERT INTO `my_sql_works`.`EmployeeSalary`
(`EmployeeID`,
`JobTitle`,
`Salary`)
VALUES
(1001, 'Salesman', 45000),
(1002, 'Receptionist', 36000),
(1003, 'Salesman', 63000),
(1004, 'Accountant', 47000),
(1005, 'HR', 50000),
(1006, 'Regional Manager', 65000),
(1007, 'Supplier Relations', 41000),
(1008, 'Salesman', 48000),
(1009, 'Accountant', 42000);
*/

INSERT INTO my_sql_works.EmployeeDemographics
(EmployeeID,
`FirstName`,
`LastName`,
 Age,
`Gender`)
VALUES
(1011, 'Ryan', 'Howard', 26, 'Male'),
(NULL, 'Holly', 'Flex', NULL, NULL),
(1013, 'Danyl', 'Phiten', NULL, 'Male'),
(NULL, NULL, NULL, NULL, NULL),
(NULL, NULL, NULL, NULL, NULL);

INSERT INTO `my_sql_works`.`EmployeeSalary`
(`EmployeeID`,
`JobTitle`,
`Salary`)
VALUES
(NULL, NULL, NULL),
(NULL, NULL, NULL),
(NULL, NULL, NULL),
(1010, NULL, 47000),
(NULL, 'Salesman', 48000);

Select * From my_sql_works.EmployeeDemographics;

Select * From my_sql_works.EmployeeSalary;