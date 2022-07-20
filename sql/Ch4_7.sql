select * from cmdev.emp right outer join cmdev.dept on cmdev.emp.deptno = cmdev.dept.deptno 
union 
select * from cmdev.emp left outer join cmdev.dept on cmdev.emp.deptno = cmdev.dept.deptno order by empno;

select * from cmdev.emp right outer join cmdev.dept on cmdev.emp.deptno = cmdev.dept.deptno where cmdev.emp.deptno is null
union
select * from cmdev.emp left outer join cmdev.dept on cmdev.emp.deptno = cmdev.dept.deptno where cmdev.emp.deptno is null
union
select * from cmdev.emp join cmdev.dept on emp.deptno = dept.deptno order by empno;

select * from cmdev.emp right outer join cmdev.dept on cmdev.emp.deptno = cmdev.dept.deptno;