select * from school.score;

select s_id , avg(s_score) from school.score group by s_id having avg(s_score) >= 60;