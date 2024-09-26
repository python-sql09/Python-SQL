CREATE DATABASE test;
USE test;
CREATE TABLE cstocks(
    date VARCHAR(10) NOT NULL,
    open FLOAT(10) NOT NULL,
    high FLOAT(10) NOT NULL,
    low FLOAT(10) NOT NULL,
    close DECIMAL(10,2) NOT NULL,
    volume INT(10) NOT NULL
);
SHOW TABLES;
select * from cstocks;
SELECT * FROM cstocks LIMIT 10;
drop table cstocks;
ALTER TABLE cstocks ADD COLUMN `Close` DECIMAL(10,2), ADD COLUMN `Volume` INT, ADD COLUMN `openInt` INT;
desc cstocks;