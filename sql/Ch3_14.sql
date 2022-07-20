select ename , dayofweek(hiredate) from cmdev.emp where dayofweek(hiredate) = 1 or dayofweek(hiredate) = 7;
select ename , dayofweek(hiredate) from cmdev.emp where dayofweek(hiredate)  in (1,7);