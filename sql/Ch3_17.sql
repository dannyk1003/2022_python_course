select * , ifnull(deptno , "need dep") from cmdev.emp;
select * , if(deptno is null , "need dep" , deptno) from cmdev.emp;
select * , if(isnull(deptno) , "need dep" , deptno) from cmdev.emp;