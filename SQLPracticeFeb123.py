# You are a border guard sitting on the Canadian border. You were given a list of travelers who have arrived at your gate today. You know that American, Mexican, and Canadian citizens don't need visas, so they can just continue their trips. You don't need to check their passports for visas! You only need to check the passports of citizens of all other countries!
# Select names, and countries of origin of all the travelers, excluding anyone from Canada, Mexico, or The US.
# travelers table schema
# name
# country
# NOTE: The United States is written as 'USA' in the table.
# NOTE: Your solution should use pure SQL. Ruby is used within the test cases just to validate your answer.

SELECT name, country 
FROM travelers 
WHERE country NOT IN ('Canada', 'Mexico', 'USA');

# Your task is to sort the information in the provided table 'companies' by number of employees (high to low). Returned table should be in the same format as provided:
# companies table schema
# id
# ceo
# motto
# employees
# Solution should use pure SQL. Ruby is only used in test cases.

SELECT * 
FROM companies
ORDER BY employees DESC;

# Given the following table 'decimals':
# ** decimals table schema **
# id
# number1
# number2
# Return a table with one column (mod) which is the output of number1 modulus number2.

SELECT number1 % number2 as mod
FROM decimals;

# For this challenge you need to create a simple SELECT statement that will return all columns from the people table WHERE their age is over 50
# people table schema
# id
# name
# age
# You should return all people fields where their age is over 50 and order by the age descending

SELECT *
FROM people
WHERE age > 50
ORDER BY age DESC;

# For this challenge you need to create a simple DISTINCT statement, you want to find all the unique ages.
# people table schema
# id
# name
# age
# select table schema
# age (distinct)

SELECT DISTINCT age
FROM people;

# In your application, there is a section for adults only. You need to get a list of names and ages of users from the users table, who are 18 years old or older.
# users table schema
# name
# age

SELECT *
FROM users
WHERE age >= 18;

# Given the following table 'decimals':
# ** decimals table schema **
# id
# number1
# number2
# Return a table with two columns (number1, number2), the value in number1 should be rounded down and the value in number2 should be rounded up.

SELECT FLOOR(number1) as number1,
CEIL(number2) as number2
FROM decimals;

# For this challenge you need to create a simple SUM statement that will sum all the ages.
# people table schema
# id
# name
# age
# select table schema
# age_sum (sum of ages)

SELECT SUM(age) as age_sum
FROM people;

# Greetings Grasshopper!
# Using only SQL, write a query that returns all rows in the custid, custname, and custstate columns from the customers table.
# Table Description for customers:
# Column	Data Type	Size	Sample
# custid	integer	8	4
# custname	string	50	Anakin Skywalker
# custstate	string	50	Tatooine
# custard	string	50	R2-D2

SELECT custid, custname, custstate
FROM customers;

# You received an invitation to an amazing party. Now you need to write an insert statement to add yourself to the table of participants.
# participants table schema
# name (string)
# age (integer)
# attending (boolean)
# NOTES:
# Since alcohol will be served, you can only attend if you are 21 or older
# You can't attend if the attending column returns anything but true

INSERT INTO participants (name, age, attending)
VALUES ('Russell Valencia', 29, TRUE);
SELECT * FROM participants;

# Given a demographics table in the following format:
# ** demographics table schema **
# id
# name
# birthday
# race

SELECT id, name, birthday, LOWER(race) as race
FROM demographics;

# Given the following table 'decimals':
# ** decimals table schema **
# id
# number1
# number2
# Return a table with two columns (root, log) where the values in root are the square root of those provided in number1 and the values in log are changed to a base 10 logarithm from those in number2.

SELECT SQRT(number1) as root, LOG(number2) as log
FROM decimals;

# Simple, remove the spaces from the string, then return the resultant string.

-- # write your SQL statement here: you are given a table 'nospace' with column 'x', return a table with column 'x' and your result in a column named 'res'.
SELECT x, REPLACE(x, ' ', '') as res
FROM nospace;