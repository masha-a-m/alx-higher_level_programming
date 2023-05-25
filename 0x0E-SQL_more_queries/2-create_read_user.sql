--fatsbase xreation
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
--new alx task 2 
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';
--task SQL create database
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;
