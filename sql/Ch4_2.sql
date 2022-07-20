select * from cmdev.emp , cmdev.dept where emp.deptno = dept.deptno;
select * from cmdev.emp left join cmdev.dept on emp.deptno = dept.deptno;