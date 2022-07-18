#select * from cmdev.emp where hiredate between "1981-02-01" and "1981-02-28";
#select * from cmdev.emp where hiredate >= "1981-02-01" and hiredate <= "1981-02-28";
select * from cmdev.emp where month(hiredate) = 2;


#select * from cmdev.emp where job = "salesman" or job = "manager";
#select * from cmdev.emp where job in ( "salesman", "manager");
