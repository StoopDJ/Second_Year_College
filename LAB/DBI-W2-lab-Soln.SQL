--SECTION 3.
-- Insert Data for Peters Pets
-- Insert statements to populate the tables

-- Customers inserted first
insert into customer (custID, custName, custEmail) values(1, 'D. Smith',  'dsmith@yahoo.co.uk	');
insert into customer (custID, custName, custEmail) values(2, 'B. Byrne', 'bb@gmail.com');
insert into customer(custID, custName) values(3, 'X. Dobbs'); -- partial insert without an email, should insert the default

-- Animals inserted next
insert into animal (animalID, animalName) values(1, 'Tiny');
insert into animal (animalID, animalName) values (2, 'Prince');
insert into animal (animalID, animalName) values(3, 'Bonnie');
insert into animal (animalID, animalName) values(4, 'CJ');
insert into animal (animalID, animalName) values(5, 'Sid');
insert into animal (animalID, animalName) values(6, 'Danger');
insert into animal (animalID, animalName) values(7, 'Sid');

-- Animal sales inserted finally
insert into animalsale (animalID, custId)  values(2,2);
insert into animalsale (animalID, custId)  values(4,2);
insert into animalsale (animalID, custId)  values(1,1);
insert into animalsale (animalID, custId)  values(5,3);
insert into animalsale (animalID, custId)  values(7,2);
-- Commit included to persist the data
commit;


--1.	Attempt to insert a row into each table that violates entity integrity.
-- this will fail because there is already a row with an id of 1 Tiny
insert into animal (animalID, animalName) values(1, 'Trigger');


--2.	Attempt to insert a row into each table that violates referential integrity.
-- This will fail because there is no customer with an id of 5
insert into animalsale (animalID, custId)  values(7,5);
--3.	Find the names of all animals.

select animalName from animal;
--4.	Find the names of all animals with an ID less than 4.
select animalname from animal where animalID <4;
--5.	Find the names of customers that contain an uppercase letter D.
select custName from customer where custName like '%D%';
--6.	Find the names of all customers that start with an uppercase letter B.
select custName from customer where custNamelike '%B%';


--SECTION 4
nsert into species(speciesCode, speciesName, speciesPrice) values (1, 'Dog', 9.99);
insert into species(speciesCode, speciesName, speciesPrice) values (2, 'Cat', 10.20);
insert into species(speciesCode, speciesName, speciesPrice) values (3, 'Snake', 20.00);
insert into species(speciesCode, speciesName, speciesPrice) values (4, 'Mouse', 5.00);

update animal set speciesCode=1 where animalID=1;
update animal set speciesCode=1 where animalID=2;
update animal set speciesCode=2 where animalID=3;
update animal set speciesCode=2 where animalID=4;
update animal set speciesCode=3 where animalID=5;
update animal set speciesCode=4 where animalID=6;
update animal set speciesCode=1 where animalID=7;
COMMIT;

