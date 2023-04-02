use employee;
CREATE TABLE login(
Uname varchar(30) UNIQUE,
Passwd varchar(20) NOT NULL,
PRIMARY KEY(Uname)
);
desc login;
Insert into login values('Trishaa','root@123');
Insert into login values('Shyam','tree@123');
Insert into login values('Rahul','yatri#234');
Insert into login values('Mohan','Kali%456');
select * from login;


