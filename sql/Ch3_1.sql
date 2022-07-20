select 1+2 , 1+"2" , "1"+"2"; # + -> math
select "2022-7-19" , "2020-07-19" , "2022/07/19" , month("2022/07/19") as month;
select null = null , null is null , null is not null , null <=> null;