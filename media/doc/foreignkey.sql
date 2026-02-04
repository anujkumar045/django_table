use homework;

create table depart(dept_id int primary key,d_name varchar(20) not null);
insert into depart(dept_id ,d_name) values(1,'DA');
insert into depart(dept_id ,d_name) values(2,'DS');
insert into depart(dept_id ,d_name) values(3,'FS');
select * from depart;


create table employee(
      emp_id int primary key,
      emp_name varchar(30) not null,
      salary decimal(10,2),
      dept_id int,
      foreign key (dept_id) references depart(dept_id)
);
insert into employee(emp_id,emp_name,salary,dept_id) values(1,'Rohit',10000,1);
insert into employee(emp_id,emp_name,salary,dept_id) values(2,'Raj',10000,1);
insert into employee(emp_id,emp_name,salary,dept_id) values(3,'Rahul',10000,3);
select * from employee;
select * from depart;