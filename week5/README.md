# Assignment - Week 5
## Task 2: Create database and table in your MySQL server

- Create a new database named website.<br>
- Create a new table named member, in the website database, designed as below:<br>
```
create database `website`;
use `website`;
create table `member`(
 `id` bigint primary key auto_increment comment'Unique ID',
 `name` varchar(255) not null comment'Name',
 `username` varchar(255) not null comment'Username',
 `password` varchar(255) not null comment'Password',
 `follower_count` int unsigned not null default 0 comment'Follower Count',
 `time` datetime not null default CURRENT_TIMESTAMP comment'Signup Time'
);
show tables;
```
![Task 2](https://github.com/Tinggg924/WeHelp-Stage1/blob/main/week5/Task%20images/Task2.png)
## Task 3: SQL CRUD
- INSERT a new row to the member table where name, username and password must
be set to test. INSERT additional 4 rows with arbitrary data.
```
insert into `member`(name,username,password) values('test','test','test');
insert into `member`(name,username,password,follower_count,time) values
('Cathie Tsai','Cathie0924','84eqet546',13487,'2024-05-01 23:07:11'),
('Alice Yang','Alice0429','%P2k7cl3s06i',333,'2024-04-03 08:02:30'),
('Penguin Yang','penguin924','@l4284Vu;3yp3u;4',4512,'2024-09-24 16:44:58'),
('Kasper Wang','brunte','vu3xoc*#x.',38,'2023-11-13 05:15:13');
```
![Task 3](https://github.com/Tinggg924/WeHelp-Stage1/blob/main/week5/Task%20images/Task3-1.png)
- SELECT all rows from the member table.
```
select * from `member`;
```
![Task 3](https://github.com/Tinggg924/WeHelp-Stage1/blob/main/week5/Task%20images/Task3-2.png)
- SELECT all rows from the member table, in descending order of time.
```
select * from `member` order by time desc;
```
![Task 3](https://github.com/Tinggg924/WeHelp-Stage1/blob/main/week5/Task%20images/Task3-3.png)
- SELECT total 3 rows, second to fourth, from the member table, in descending order
of time. Note: it does not mean SELECT rows where id are 2, 3, or 4.
```
select * from `member`order by time desc limit 3 offset 1;
```
![Task 3](https://github.com/Tinggg924/WeHelp-Stage1/blob/main/week5/Task%20images/Task3-4.png)
- SELECT rows where username equals to test.
```
select * from `member` where username = 'test';
```
![Task 3](https://github.com/Tinggg924/WeHelp-Stage1/blob/main/week5/Task%20images/Task3-8.png)
- SELECT rows where name includes the es keyword.
```
select * from `member` where name like '%es%';
```
![Task 3](https://github.com/Tinggg924/WeHelp-Stage1/blob/main/week5/Task%20images/Task3-5.png)
- SELECT rows where both username and password equal to test.
```
select * from `member` where username = 'test' and password = 'test';
```
![Task 3](https://github.com/Tinggg924/WeHelp-Stage1/blob/main/week5/Task%20images/Task3-6.png)
- UPDATE data in name column to test2 where username equals to test.
```
SET SQL_SAFE_UPDATES = 0;
update member SET name = "test2" where username = "test";
```
![Task 3](https://github.com/Tinggg924/WeHelp-Stage1/blob/main/week5/Task%20images/Task3-7.png)

## Task 4: SQL Aggregation Functions
-  SELECT how many rows from the member table.
```
select count(*) from `member`;
```
![Task 4](https://github.com/Tinggg924/WeHelp-Stage1/blob/main/week5/Task%20images/Task4-1.png)

- SELECT the sum of follower_count of all the rows from the member table.
```
select SUM(follower_count) from `member`;
```
![Task 4](https://github.com/Tinggg924/WeHelp-Stage1/blob/main/week5/Task%20images/Task4-2.png)

- SELECT the average of follower_count of all the rows from the member table.
```
select AVG(follower_count) from `member`;
```
![Task 4](https://github.com/Tinggg924/WeHelp-Stage1/blob/main/week5/Task%20images/Task4-3.png)

- SELECT the average of follower_count of the first 2 rows, in descending order of
follower_count, from the member table.
```
select AVG(follower_count)
from (
    select follower_count
    from `member`
    order by follower_count DESC
    LIMIT 2
) as subquery;
```
![Task 4](https://github.com/Tinggg924/WeHelp-Stage1/blob/main/week5/Task%20images/Task4-4.png)

## Task 5: SQL JOIN
- Create a new table named message, in the website database. designed as below:
```
use `website`;
create table `message` (
  `id` bigint primary key auto_increment comment 'Unique ID',
  `member_id` bigint not null comment 'Member ID for Message Sender', 
  foreign key (`member_id`) references `message`(`id`),
  `content` varchar(255) not null comment 'Content',
  `like_count` int unsigned not null default 0 comment 'Like Count',
  `time` datetime not null default CURRENT_TIMESTAMP comment 'Publish Time'
);
```
![Task 5](https://github.com/Tinggg924/WeHelp-Stage1/blob/main/week5/Task%20images/Task5-1.png)

- SELECT all messages, including sender names. We have to JOIN the member table
to get that.
```
select `message`.*, member.name as sender_names from `message` inner join member ON `member`.id = `message`.member_id;
```
![Task 5](https://github.com/Tinggg924/WeHelp-Stage1/blob/main/week5/Task%20images/Task5-2.png)

- SELECT all messages, including sender names, where sender username equals to
test. We have to JOIN the member table to filter and get that.
```
select `message`.*, member.name as sender_names from `message` inner join member ON `member`.id = `message`.member_id where username = 'test';
```
![Task 5](https://github.com/Tinggg924/WeHelp-Stage1/blob/main/week5/Task%20images/Task5-3.png)

- Use SELECT, SQL Aggregation Functions with JOIN statement, get the average like
count of messages where sender username equals to test.
```
select AVG(`message`.like_count) from (`message` inner join member ON `member`.id = `message`.member_id) where `member`.username = 'test';
```
![Task 5](https://github.com/Tinggg924/WeHelp-Stage1/blob/main/week5/Task%20images/Task5-4.png)

-  Use SELECT, SQL Aggregation Functions with JOIN statement, get the average like
count of messages GROUP BY sender username.
```
select `member`.username as sender_names, AVG(`message`.like_count) as average_like_count from `message` inner join member ON `member`.id = `message`.member_id group by member.username;
```
![Task 5](https://github.com/Tinggg924/WeHelp-Stage1/blob/main/week5/Task%20images/Task5-5.png)
