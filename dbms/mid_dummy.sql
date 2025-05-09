

SELECT 
    e2.first_name AS employee2,
    e1.manager_id
FROM 
    employees e1
JOIN 
    employees e2 ON e1.manager_id = e2.manager_id
WHERE 
    e1.employee_id < e2.employee_id
    AND e1.manager_id IS NOT NULL;
    
    



select * from employees where manager_id=100;