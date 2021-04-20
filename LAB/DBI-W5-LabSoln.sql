--1. Create Table
Create Table Customer(
custID number (6) , 
custName varchar2(50) not null, 
custPhone varchar2(30) not null, 
custEmail varchar2(30),
constraint chk_cemail check(custemail like '%@%'),
constraint storeCust_pk primary key (custID)
);

--2. Populate Customer with data
insert into Customer (custID, custName, custPhone, custEmail) values(
1001,	'A.	Green',	'01 402 2849','agreen@mail.com');
insert into Customer (custID, custName, custPhone, custEmail) values(
1002, 'J. Keogh',	'02 203 7896',	'jkeogh@mail.com');
insert into Customer (custID, custName, custPhone) values(
1003, 'K. Jones',	'03 333 8888');
commit;

--3. Add column for customer to appRepair
alter table appRepair add customer_id number(6);

--4. Update appRepair data with customer IDs
update appRepair set customer_id=1001 where serialNo=9001;
update appRepair set customer_id=1002 where serialNo=9002;
update appRepair set customer_id=1002 where serialNo=9003;
commit;

--5. Add Foreign Key constraint to appRepair to ensure consistency with customer.
alter table apprepair add constraint appRepair_cust_fk FOREIGN KEY (customer_id) REFERENCES customer(custID);

--6.	Write the SQL to output the name of each customer in uppercase.
select upper(custname) "CUSTOMER NAME"
from customer;

--7.	Write the SQL to output the sale date of each appliance formatted DDTH MONTH YY (using TO_CHAR).
select  TO_CHAR(appSaleDate, 'fmDDTH MONTH YY') SALEDATE
from appliance ;

--8.	Write the SQL to output the price of each appliance repair formatted to include the local currency symbol 
--and formatted as 5 digits followed by two decimal places.
select TO_CHAR(repairCost, 'fm99999.99') "REPAIR COST"
from apprepair;

--9.	Write the SQL to output for each customer their email address or ‘No Email provided’ 
--if the email address is null (use NVL).
select nvl(custemail, 'No Email Provided') "Email Address"
from customer;

--10. Write  the SQL to output for each customer 'Email Provided' if the customer has provided and email 
-- address  or ‘No Email provided’ if the email address is null (use NVL2).
select nvl2(custemail, 'Email Provided',  'No Email Provided')
from customer;

--11. Write the SQL to retrieve for each appliance submitted for repair its serial number 
--and the name and email address of the customer who requested the repair.  (JOIN required)
select serialNo, custname, custemail 
from appRepair
join customer ON customer_id=custID;

--12. Write the SQL to retrieve to retrieve for each appliance submitted for repair its serial number,
-- description, date of sale and the name and email address of the customer who requested the repair. 
-- (JOIN to two tables required)
select serialNo, appDesc, appSaleDate,custname, custemail 
from appRepair
join customer ON customer_id=custID
join appliance using(serialNo);

--13. Write the SQL to retrieve to retrieve for each appliance submitted for repair its serial number, 
--description, date of sale and the name and email address of the customer who requested the repair.  
--(JOIN to two tables required). 
--Format your output so that the customer name is in uppercase and the date of sale is formatted as DDTH MONTH YY (use TO_CHAR).
select serialNo, appDesc, TO_CHAR(appSaleDate, 'fmDDTH MONTH YY'), upper(custname), custemail 
from appRepair
join customer ON customer_id=custID
join appliance using(serialNo);

--14.	Write the SQL to retrieve to retrieve for each appliance submitted for repair its serial number, description, date of sale,  the name of the customer who requested the repair, the description of the repair plus the cost of the repair.  (JOIN to two tables required). 
--Format the output so that it is output in sentences as follows:

--"The repair to appliance 9001 DVD Player,  sold on 1ST JANUARY 2018 to A.GREEN, to solve the issue DVD  Stuck, which will cost 67.50".

--Ensure that zeros are output if no decimal value exists.
select 'The repair to appliance ' || serialNo || ' ' || appDesc|| ', sold on ' || TO_CHAR(appSaleDate, 'fmDDTH MONTH YY') || ' to '|| upper(custname) ||  
' , to solve the issue ' || repairDesc || ' will cost ' || TO_CHAR(repairCost, 'fmU99999.00')
from appRepair
join customer ON customer_id=custID
join appliance using(serialNo);

