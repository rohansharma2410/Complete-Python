show databases;

create database legend
USE  legend

'''create table'''
CREATE TABLE if not exists Bank(
age int,
job varchar(30),
marital varchar(30),
education varchar (30),
`default` varchar (30),
balance int ,
housing varchar(30),
loan varchar(30),
contact varchar(30), 	
`day` int,
`month` varchar(20),
duration varchar(20),
campaign varchar(20),
pdays int,
previous int,
poutcome varchar(30),
y varchar(30)
'''see table'''
show tables
'''see data type and details table''' 
describe Bank
'''load data to table'''
INSERT INTO Bank VALUES(58,"management","married","tertiary","no",2143,"yes","no","unknown",5,"may",261,1,-1,0,"unknown","no"),
(58,"management","married","tertiary","no",2143,"yes","no","unknown",5,"may",261,1,-1,0,"unknown","no"),
(44,"technician","single","secondary","no",29,"yes","no","unknown",5,"may",151,1,-1,0,"unknown","no"),
(33,"entrepreneur","married","secondary","no",2,"yes","yes","unknown",5,"may",76,1,-1,0,"unknown","no"),
(47,"blue-collar","married","unknown","no",1506,"yes","no","unknown",5,"may",92,1,-1,0,"unknown","no"),
(33,"unknown","single","unknown","no",1,"no","no","unknown",5,"may",198,1,-1,0,"unknown","no"),
(35,"management","married","tertiary","no",231,"yes","no","unknown",5,"may",139,1,-1,0,"unknown","no"),
(28,"management","single","tertiary","no",447,"yes","yes","unknown",5,"may",217,1,-1,0,"unknown","no"),
(42,"entrepreneur","divorced","tertiary","yes",2,"yes","no","unknown",5,"may",380,1,-1,0,"unknown","no"),
(58,"retired","married","primary","no",121,"yes","no","unknown",5,"may",50,1,-1,0,"unknown","no"),
(43,"technician","single","secondary","no",593,"yes","no","unknown",5,"may",55,1,-1,0,"unknown","no"),
(41,"admin.","divorced","secondary","no",270,"yes","no","unknown",5,"may",222,1,-1,0,"unknown","no"),
(29,"admin.","single","secondary","no",390,"yes","no","unknown",5,"may",137,1,-1,0,"unknown","no"),
(53,"technician","married","secondary","no",6,"yes","no","unknown",5,"may",517,1,-1,0,"unknown","no"),
(58,"technician","married","unknown","no",71,"yes","no","unknown",5,"may",71,1,-1,0,"unknown","no"),
(57,"services","married","secondary","no",162,"yes","no","unknown",5,"may",174,1,-1,0,"unknown","no"),
(51,"retired","married","primary","no",229,"yes","no","unknown",5,"may",353,1,-1,0,"unknown","no"),
(45,"admin.","single","unknown","no",13,"yes","no","unknown",5,"may",98,1,-1,0,"unknown","no"),
(57,"blue-collar","married","primary","no",52,"yes","no","unknown",5,"may",38,1,-1,0,"unknown","no"),
(60,"retired","married","primary","no",60,"yes","no","unknown",5,"may",219,1,-1,0,"unknown","no")


SELECT * FROM Bank

select * from Bank
select age , job from  Bank 
select `default` , age from  Bank 
select * from Bank where  age = 41
select job from Bank where age =41


select * from Bank where job = 'retired' and balance > 100

select * from Bank where education = 'primary' or balance < 100


select * from Bank where education = 'primary' and  balance < 100

select distinct job from  Bank

select * from Bank order by age

select count(*) from Bank

select sum(balance) from Bank

select * from Bank where  balance = (select min(balance) from Bank ) 

SELECT marital,count(*) from Bank group by marital 

SELECT marital,count(*), sum(balance) from Bank group by marital 

SELECT marital,count(*), sum(balance) from Bank group by marital having sum(balance >300)

select * from Bank

set sql_safe_updates = 0 
update Bank set balance = 0 where job = 'unknown'

select * from Bank
set sql_safe_updates = 0 
update Bank set contact = 'known' , y = 'yes' where month = 'may'

update Bank set `default` = 'NULL' where `default`= 'no'

delete from Bank where job='unknown'

select * from Bank
'''procures'''
DELIMITER && 
create procedure select_pro()
BEGIN
	select * from Bank;
END &&

call select_pro()
'''proceure for specific conditions'''
DELIMITER &&  
create procedure select_pre_filter() 
BEGIN
	select * from Bank where job = 'retired' and balance > 100;
END &&  

call select_pre_filter()
'''proecures passing paramenters with 1 variable  '''
DELIMITER &&  
create procedure select_pre_filter1(IN var int) 
BEGIN
	select * from Bank where job = 'retired' and balance > var;
END &&  

call select_pre_filter1(200)



'''proecures passing paramenters with 2 variable'''
DELIMITER &&  
create procedure select_pre_filter2(IN var int ,IN var1 varchar(30)) 
BEGIN
	select * from Bank where job = var1 and balance > var;
END &&  

call select_pre_filter2(100 ,'services' )

'''sql views'''

select * from (select  job , age , education , y from Bank ) as a where a.age = 58#fetch dats from subset of table

select job , age , education, y from Bank where age = 58 #fetch data from entire table

create view bank_view as select  job , age , education , y from Bank
select * from bank_view where age = 58
'''views virtaul table or subset of table '''

'''creating a new table'''
CREATE TABLE if not exists Bank2(
age int,
job varchar(30),
marital varchar(30),
education varchar (30),
`default` varchar (30),
balance int ,
housing varchar(30),
loan varchar(30),
contact varchar(30), 	
`day` int,
`month` varchar(20),
duration varchar(20),
campaign varchar(20),
pdays int,
previous int,
poutcome varchar(30),
y varchar(30))


show tables

insert into Bank2 select * from Bank ;

select * from Bank2

'''joins'''

select Bank.age , Bank.job , Bank.marital from Bank inner join Bank2 on Bank.age =Bank2.age

select * from Bank
select Bank.age , Bank.job , Bank.marital from Bank right join Bank2 on Bank.age =Bank2.age
select * from Bank
select Bank.age , Bank.job , Bank.marital from Bank left join Bank2 on Bank.age =Bank2.age










 