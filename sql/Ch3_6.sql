select ename , concat(left(ename,1) , lower(substring(ename,2,length(ename)))) from cmdev.emp; # ename first upper, other lower
select ename , concat(left(ename,1) , lower(substring(ename,2))) from cmdev.emp; # ename first upper, other lower
select ename , replace(lower(ename) , left(lower(ename),1),upper(left(ename,1))) from cmdev.emp; # use replace