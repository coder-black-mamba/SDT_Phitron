use test_db;
-- 1
drop table Student;
drop table `Library`;
drop table Fees;

create table Student (
id int primary key not null ,
name varchar(100) not null,
roll char(4) not null unique,
reg char(6) not null unique,
age int,
class varchar(100) not null,
check (age > 3)
);


create table `Library`(
	id int primary key not null,
    name varchar(100) not null,
    author varchar(100) not null,
    student_id int not null,
    foreign key (student_id) references Student(id)
);

create table Fees (
	id int primary key not null,
    amount decimal(10,2) not null,
    last_date date not null,
    student_id int not null,
    foreign key (student_id) references Student(id)
);
set sql_safe_updates=0;

-- 2.
-- 3.
-- Diff Between Data And Information
-- 4

-- 5
create table Employee(
	EmployeeID int primary key auto_increment ,
    FirstName varchar(20) not null,
	LastName varchar(20) not null,
    Age int ,
    Department varchar(50)

);

INSERT INTO Employee (EmployeeID, FirstName, LastName, Age, Department) VALUES
(1, 'John', 'Doe', 28, 'Sales'),
(2, 'Jane', 'Smith', 32, 'Marketing'),
(3, 'Michael', 'Johnson', 35, 'Finance'),
(4, 'Sarah', 'Brown', 30, 'HR'),
(5, 'William', 'Davis', 25, 'Engineering'),
(6, 'Emily', 'Wilson', 28, 'Sales'),
(7, 'Robert', 'Lee', 33, 'Marketing'),
(8, 'Laura', 'Hall', 29, 'Finance'),
(9, 'Thomas', 'White', 31, 'HR'),
(10, 'Olivia', 'Clark', 27, 'Engineering');

-- select distinct Department from employee ;
-- select LastName from Employee order by Age desc  ;
-- select LastName from Employee where Age > 30 and Department = "Marketing";
-- select * from Employee;
-- select * from Employee where inc
-- select * from employee where Department="Engineering";
select * from Employee where FirstName like "%son%" or LastName like "%son%";
select * from employee;
SELECT * FROM Employee 
WHERE FirstName LIKE '%son%' OR LastName LIKE '%son%';
