select * from school.score;
select max(s_score) , min(s_score) from school.score;
select * from school.score where s_score = (select max(s_score) from school.score) or s_score = (select min(s_score) from school.score);

select * from school.score order by s_score limit 1;