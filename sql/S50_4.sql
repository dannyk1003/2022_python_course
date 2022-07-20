#查出各課程成績最高和最低的分數，需顯示課程代號、最高分與最低分

/*
select * from school.score;
select * from school.course;
select * from school.score , school.course where school.score.c_id = school.course.c_id;
*/
select course.c_id , max(s_score) , min(s_score) from school.score , school.course where school.score.c_id = school.course.c_id group by school.course.c_name;

#查出課程編號02成績比課程編號01成績低分的所有同學學號
select * from school.score group by school.score.s_id having school.score.c_id = "01" ;
#select s_id , c_id , s_score from school.score where school.score.c_id = 2;
#select s_id score, c_id , s_score from school.score where school.score.c_id = 1;
#select max(s_score) from school.score where school.score.c_id = "02" or school.score.c_id = "01" group by s_id;


#select * , s_score from school.score where school.score.c_id = "02";

#select * , s_score from school.score where school.score.c_id = "01";
