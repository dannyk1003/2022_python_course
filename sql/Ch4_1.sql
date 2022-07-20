#select * from world.city , world.country;
select * from world.city , world.country where country.capital = city.ID order by ID;