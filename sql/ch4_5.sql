select * from cmdev.emp right outer join cmdev.dept on cmdev.emp.deptno = cmdev.dept.deptno;

/*
select * from cmdev.emp right outer join cmdev.dept on cmdev.emp.deptno = cmdev.dept.deptno 
union 
select * from cmdev.emp left outer join cmdev.dept on cmdev.emp.deptno = cmdev.dept.deptno order by empno;
*/