select * from employees where manager_id=100 ;


select * from departments;
select * from Course;
select * from Instructor;
select * from Student;

with std_course_count as (
select StudentId , count(CourseID) 
as course_count from 
Enrollment group by StudentId
)

select * from std_course_count SCC 
join Student S on 
SCC.StudentID=S.StudentID 
where SCC.course_count>2 ;
-- 5 ->. 10
select InstructorID , count(*) from Course group by InstructorID;
select * from Course order by credits desc;











