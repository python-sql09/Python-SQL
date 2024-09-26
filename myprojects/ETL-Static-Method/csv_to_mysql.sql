USE test;
CREATE TABLE stocks(
    date VARCHAR(10) NOT NULL,
    open FLOAT(10) NOT NULL,
    high FLOAT(10) NOT NULL,
    low FLOAT(10) NOT NULL,
    close DECIMAL(10,2) NOT NULL,
    volume INT(10) NOT NULL
);
SHOW TABLES;
select * from stocks;