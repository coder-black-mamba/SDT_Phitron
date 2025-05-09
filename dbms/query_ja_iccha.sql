use company_db;
-- select * from employees;
-- select * from departments ;

-- select first_name,last_name from employees where department_id=(select department_id from departments where name="HR");
-- inner join
-- select e.first_name,e.last_name ,d.name as department from employees e inner join departments d on e.department_id = d.id;

-- select e.first_name,e.last_name , d.name as department from employees e left join departments d on e.department_id = e.id;
SELECT 
  e.first_name, 
  e.last_name, 
  d.name AS department
FROM employees e
RIGHT JOIN departments d 
  ON e.department_id = d.id;

