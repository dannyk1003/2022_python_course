select * from school.course;
select * from school.teacher;

select count(c_name) from school.course;
select t_id , count(c_name) from course group by t_id;