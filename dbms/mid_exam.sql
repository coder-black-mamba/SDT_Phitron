-- 1.
-- Primary Key is a column or set of columns that uniquely indentifies each row in a table. It cannot have NULL values .
-- Where as , foreign key is a column in one table that references primary key from another table. It used to create relationship between the two tables.
-- 2.
-- A self join is like regular join but unlike regular join , it joins on the same table .-- 
-- A self join is a type of join where a table is joined with itself. 
use dummydb;


select 
    distinct e1.first_name as employee_name,
    e1.manager_id
from 
    employees e1
join 
    employees e2 ON e1.manager_id = e2.manager_id
where 
    e1.employee_id != e2.employee_id
order by e1.manager_id ;

-- select distinct e1.first_name as first_name,e1.manager_id as manager_id 
-- from employees e1 join employees e2 
-- on 
-- e1.manager_id=e2.manager_id ;

select e1.first_name as emp1,e2.first_name as emp2, e1.manager_id
    from employees e1
    join employees e2 on e1.manager_id = e2.manager_id
    where e1.employee_id<e2.employee_id
	order by e1.manager_id , e1.first_name,e2.first_name ;

select * from employees;

-- SELECT 
--     e2.first_name AS employee2,
--     e1.manager_id
-- FROM 
--     employees e1
-- JOIN 
--     employees e2 ON e1.manager_id = e2.manager_id
-- WHERE 
--     e1.employee_id < e2.employee_id
--     AND e1.manager_id IS NOT NULL;

-- 3.
/*
Employee_Id
First Name
Last Name
Date of Birth
Department Id
Salary


*/ 
create table Employees
 (
	Employee_Id int primary key auto_increment not null,
	First_Name varchar(50) not null,
	Last_Name varchar(50) not null,
    Date_Of_Birth date,
	Department_Id int ,
	Salary decimal(10,2)
 );
 
 
 create table Projects 
 (
	Project_Id int primary key auto_increment not null,
    Project_Name varchar(100) not null,
    Start_Date date,
    End_Date date,
    Budget decimal(15,2)
 );
 
 create table Employee_Projects
 (
	Employee_Id int not null ,
    Project_Id int not null,
    primary key (Employee_Id , Project_Id),
    foreign key (Employee_Id) references Employees(Employee_Id),
    foreign key (Project_Id) references Projects(Project_Id)
 );
 
 select e.First_Name,e.Last_Name , p.Project_Name from Employees e join Employee_Projects ep on e.Employee_Id=ep.Employee_Id join Projects p on  ep.Project_Id=p.Project_Id;
 
 
 /*
 Using the dummydb, write an SQL query to get the third-highest salary in the employees table.
 */
 
 -- 1
 select distinct salary from employees order by salary desc limit 2,1;
 
 
 -- 2
 select max(salary) 
	from employees 
    where 
    salary<(select max(salary) from employees
		where salary < (select max(salary) 
        from employees));
 
 
/*
Write a query to show the department names and the number of employees in each department.
*/
 
 
 select * from departments;
 
 
 select 
	d.department_id , 
    d.department_name 
    , count(e.employee_id) as Employee_Count 
    from employees e
	left join departments d 
	on e.department_id = d.department_id
	group by department_id
;

-- 6
/*
Illustrate INNER JOIN, LEFT JOIN, RIGHT JOIN, 
and CROSS JOIN with examples using the employees 
and departments tables.

*/
-- innner join
select e.first_name , e.last_name,d.department_name 
from employees e 
inner join departments d 
on e.department_id=d.department_id;



-- left join
select e.first_name , e.last_name,d.department_name 
from employees e 
left join departments d 
on e.department_id=d.department_id;


-- right join
select  d.department_name , e.first_name , e.last_name
from employees e 
right join departments d 
on e.department_id=d.department_id;


-- cross join
select e.first_name , e.last_name,d.department_name 
from employees e 
cross join departments d ;


-- 7
/*
What is a Common Table Expression (CTE)? 
Write an example query using CTE to show the names
 of employees whose salary is higher than the average salary.


In SQL, a Common Table Expression (CTE) is an essential tool for 
simplifying complex queries and making them more readable. 
By defining temporary result sets that can be referenced multiple times, 
a CTE in SQL allows developers to break down complicated logic into manageable parts.
 CTEs help with hierarchical data representation, improve code reusability,
 and simplify maintenance. 

CTE(Common Table Expression) is a named result set which is like a temporary table on which we can use SELECT,INSERT,UPDATE
,DELETE statement . It exists only in the time of execution


A Common Table Expression (CTE) is a temporary, 
named result set that exists only during the execution of a single SQL statement.
 It helps improve the readability and organization of complex queries.
 A CTE is defined using the WITH clause and can be used like a temporary table within a query.
*/

with average_salary as (
	select avg(salary) as avg_salary from employees 
)

select first_name,last_name,salary
 from employees 
 where salary >(select avg_salary from average_salary);

-- 8
select first_name , last_name , salary  from employees where salary <(
	select salary
	from employees 
    where first_name="Steven" and last_name="King"
    ) ;

-- 9



select d.department_name,e.first_name,e.last_name
 from departments d 
 join employees e
 on d.manager_id = e.employee_id ;

-- 10 
select distinct d.department_name , l.city 
from departments d 
join locations l 
on d.location_id = l.location_id;




 
 
 
 
 
 