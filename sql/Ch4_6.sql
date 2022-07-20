use world;
select Region , Name , Population from world.country where country.Region = "Southeast Asia" and country.Population < 2000000
union
select Region , Name , Population from world.country where country.Region = "Eastern Asia" and country.Population < 1000000;
 