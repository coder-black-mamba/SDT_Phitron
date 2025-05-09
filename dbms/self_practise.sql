-- 🎯 Your Turn: Mini Challenges

--     List all employees with their project names.

--     List all projects with employee names who work on them.

--     List departments and total number of employees in each (use JOIN + GROUP BY).

use company_db;
-- select e.first_name , e.last_name ,p.name from employees e inner join projects p on e.id = p.id

-- select 
-- 	e.first_name ,
-- 	e.last_name ,
--     p.name as project_name
--     from 
--     employees e 
--     inner join 
--     projects p 
--     on 
--     (select project_id from employee_projects where employee_id=e.id) 
--     = 
--     p.id


-- select 
-- 	e.first_name,
--     e.last_name,
--     p.name as project_name
-- from employees e 
-- join employee_projects ep on e.id = ep.employee_id
-- join projects p on ep.project_id=p.id;-- 

-- select 
-- 	p.name as project_name,
-- 	e.first_name,
--     e.last_name
-- from employees e 
-- join employee_projects ep on e.id = ep.employee_id
-- join projects p on ep.project_id=p.id;


-- SELECT 
--     p.name AS project_name,
--     e.first_name,
--     e.last_name
-- FROM projects p
-- JOIN employee_projects ep ON p.id = ep.project_id
-- JOIN employees e ON ep.employee_id = e.id;



select 
count(d.id) as total_employee, d.name 
from departments d 
inner join employees e 
on d.id=e.department_id group by d.id;




