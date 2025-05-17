-- https://docs.google.com/document/d/1PYQyt8TzP_Iwv4FtOKEmLU13whsae_40BxKEE_tExIg/edit?tab=t.0
use courses_db;

show tables;
/*
The most challenging topic was understanding complex SQL joins and subqueries.
 It was confusing at first to link multiple tables correctly. 
 I overcame it by practicing simple examples, 
drawing table relationships, and using online SQL practice platforms.
*/

create table Instructor (	
    InstructorID int auto_increment primary key,	
    Name varchar(255) not null,	
    Email varchar(255) not null unique,	
    Phone varchar(15),	
    Department varchar(50)	
);	

create table Course (	
    CourseID int auto_increment primary key,	
    Title varchar(255) not null,	
    Credits int not null,	
    InstructorID int,	
    foreign key (InstructorID) references Instructor(InstructorID) on delete cascade	
);	
CREATE TABLE Student (	
    StudentID INT AUTO_INCREMENT PRIMARY KEY,	
    Name VARCHAR(255) NOT NULL,	
    Email VARCHAR(255) NOT NULL UNIQUE,	
    Phone VARCHAR(15)	
);
CREATE TABLE Enrollment (	
    EnrollmentID INT AUTO_INCREMENT PRIMARY KEY,	
    StudentID INT,	
    CourseID INT,	
    EnrollmentDate DATE NOT NULL,	
    FOREIGN KEY (StudentID) REFERENCES Student(StudentID),	
    FOREIGN KEY (CourseID) REFERENCES Course(CourseID)	
);	





-- Insert Instructors
INSERT INTO Instructor (Name, Email, Phone, Department) VALUES
('Dr. Alice Smith', 'alice.smith@university.edu', '1234567890', 'Computer Science'),
('Dr. Bob Johnson', 'bob.johnson@university.edu', '1234567891', 'Mathematics'),
('Dr. Clara Davis', 'clara.davis@university.edu', '1234567892', 'Physics');

-- Insert Students
INSERT INTO Student (Name, Email, Phone) VALUES
('John Doe', 'john.d6dsoe@student.edu', '5551234567'),
('Jane Roe', 'jane.r5sdfoe@student.edu', '5552345678'),
('Mike Brown', 'mike.bsdfr4own@student.edu', '5553456789'),
('Sara White', 'sara.wh3dfite@student.edu', '5554567890'),
(' POreAdded', 'sara.whitsdf2e@student.edu', '5554567890');

INSERT INTO Student (StudentID,Name, Email, Phone) VALUES
(5,'pore Doe', 'john.d6dsasdoe@student.edu', '5551234567');

-- Insert Courses
INSERT INTO Course (Title, Credits, InstructorID) VALUES
('Introduction to Programming', 3, 1),
('Calculus I', 4, 2),
('Physics Fundamentals', 3, 3),
('Data Structures', 3, 1);

-- Insert Enrollments
INSERT INTO Enrollment (StudentID, CourseID, EnrollmentDate) VALUES
(1, 1, '2025-01-15'),
(2, 1, '2025-01-16'),
(3, 2, '2025-01-17'),
(4, 3, '2025-01-18'),
(1, 4, '2025-01-19'),
(2, 3, '2025-01-20');



select * from student;

insert into Enrollment (StudentID,CourseID,EnrollmentDate)
select 5,CourseID ,'2025-05-16'
from course 
order by Credits desc
limit 1;

select * from Enrollment;
select * from course;
select * from Instructor;

update Course
set InstructorID=3 
where CourseID=3;
SET SQL_SAFE_UPDATES=0; 


select I.Name , sum(C.Credits) as TotalCredits
from Course C join 
Instructor I on 
C.InstructorID=I.InstructorID
group by I.InstructorID
having TotalCredits=
(
	select MAX(Total)
    from (
		select sum(credits) as Total
        from Course 
        group by InstructorID
    )
    as CreditTotals
);



with ins_id_cred as (
select InstructorID, sum(Credits) as TotalCredits
from Course
group by InstructorID
order by TotalCredits DESC
limit 1
)

select I.Name , IIC.TotalCredits
 from Instructor I Join
 ins_id_cred IIC 
 on I.InstructorID=IIC.InstructorID;



with students as (
select InstructorID, sum(Credits) as TotalCredits
from Course
group by InstructorID
order by TotalCredits DESC
limit 1
)

select I.Name , IIC.TotalCredits
 from Instructor I Join
 ins_id_cred IIC 
 on I.InstructorID=IIC.InstructorID;


select max(Salary) as SecondHighest
from Instructor 
where salary<(
	select max(salary) 
	from Instructor
);
 







