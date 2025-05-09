use company_db;

show tables;

INSERT INTO departments (name) VALUES 
('Engineering'), 
('HR'), 
('Sales'), 
('Finance');


INSERT INTO employees (first_name, last_name, department_id, manager_id, hire_date) VALUES
('Alice', 'Johnson', 1, NULL, '2018-03-12'),   -- Alice is a manager
('Bob', 'Smith', 1, 1, '2019-07-01'),
('Charlie', 'Lee', 2, NULL, '2017-01-01'),     -- Charlie is a manager
('David', 'Brown', 2, 3, '2020-09-15'),
('Fahmida', 'Eva', 3, NULL, '2021-04-25'),       -- Eva is a manager
('Frank', 'Wilson', 3, 5, '2022-06-30');


INSERT INTO salaries (employee_id, amount, effective_from) VALUES
(1, 80000, '2022-01-01'),
(2, 60000, '2022-01-01'),
(3, 85000, '2022-01-01'),
(4, 50000, '2022-01-01'),
(5, 75000, '2022-01-01'),
(6, 55000, '2022-01-01');

INSERT INTO projects (name, start_date, end_date) VALUES
('Website Redesign', '2023-01-01', '2023-06-30'),
('HR System Upgrade', '2023-02-01', '2023-07-31'),
('Salesforce Migration', '2023-03-01', '2023-08-31');

INSERT INTO employee_projects (employee_id, project_id, role) VALUES
(1, 1, 'Lead Developer'),
(2, 1, 'Backend Developer'),
(3, 2, 'HR Consultant'),
(4, 2, 'HR Assistant'),
(5, 3, 'Sales Manager'),
(6, 3, 'Sales Associate');
