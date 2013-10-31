-- SELECT * FROM person;

-- SELECT name, age FROM pet;

-- SELECT name, age FROM pet WHERE dead = 0;

-- SELECT * FROM person WHERE first_name != "Zed";

-- SELECT name, breed, age FROM pet WHERE age > 10;

-- SELECT * from person WHERE age > (SELECT age FROM person WHERE first_name = "Carl");

SELECT * from person WHERE age > (SELECT age FROM person WHERE first_name = "Carl") AND first_name = "Zed";