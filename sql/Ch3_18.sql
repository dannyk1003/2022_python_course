select job , max(salary) , min(salary) , count(salary) , avg(salary) , sum(salary) from cmdev.emp group by job order by job;

select job , max(salary) , min(salary) , count(salary) , avg(salary) , sum(salary) from cmdev.emp group by job having avg(salary) > 2500 order by job;
#select distinct job , max(salary) from cmdev.emp;