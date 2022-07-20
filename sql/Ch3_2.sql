set @a = "Hello";
select lower(@a) , upper(@a) , lpad(@a, 10, "0") , rpad(@a, 10, "0"); # lowercase and uppercase , front and back fill 0
select @a , concat("     " , @a , "   ") , trim(concat("   ",@a,"   "));
select repeat("Hi" , 5), replace(@a , "He" , "she");