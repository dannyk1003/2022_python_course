select * , 
case 
	when salary > 3000 then "high" 
	when salary between 1000 and 3000 then "normal"
	when salary < 1000 then "low"
end as salary_level
from cmdev.emp;
