create database craftbeerDB;

use craftbeerDB;

create table breweries (
   brewery_id INT PRIMARY KEY,
   name VARCHAR(100),
   city VARCHAR(100),
   state VARCHAR(10)
);

create table beer (
   id INT PRIMARY KEY,
   brewery_id INT,
   abv DOUBLE,
   ibu double,
   name VARCHAR(100) character set utf8,
   style VARCHAR(100) character set utf8,
   ounces DOUBLE
);
