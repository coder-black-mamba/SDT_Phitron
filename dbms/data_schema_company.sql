use company_db;
create table departments (
id INT KEY AUTO_INCREMENT,
name VARCHAR(100) NOT NULL
);


create table employees(
id INT PRIMARY KEY AUTO_INCREMENT,
first_name VARCHAR(100),
last_name VARCHAR(100),
department_id INT,
manager_id INT,
hire_date DATE,
foreign key(department_id) references departments(id),
foreign key(manager_id) references employees(id)
);

create table salaries(
	id int primary key auto_increment,
    employee_id INT,
    amount DECIMAL(10,2),
    effective_from date,
    foreign key (employee_id) references employees(id)
    
);


CREATE TABLE projects (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    start_date DATE,
    end_date DATE
);

CREATE TABLE employee_projects (
    employee_id INT,
    project_id INT,
    role VARCHAR(100),
    PRIMARY KEY (employee_id, project_id),
    FOREIGN KEY (employee_id) REFERENCES employees(id),
    FOREIGN KEY (project_id) REFERENCES projects(id)
);
