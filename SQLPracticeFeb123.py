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