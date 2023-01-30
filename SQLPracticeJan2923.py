# A country is big if:
# it has an area of at least three million (i.e., 3000000 km2), or
# it has a population of at least twenty-five million (i.e., 25000000).
# Write an SQL query to report the name, population, and area of the big countries.
# Return the result table in any order.
# The query result format is in the following example.
# Example 1:
# Input: 
# World table:
# +-------------+-----------+---------+------------+--------------+
# | name        | continent | area    | population | gdp          |
# +-------------+-----------+---------+------------+--------------+
# | Afghanistan | Asia      | 652230  | 25500100   | 20343000000  |
# | Albania     | Europe    | 28748   | 2831741    | 12960000000  |
# | Algeria     | Africa    | 2381741 | 37100000   | 188681000000 |
# | Andorra     | Europe    | 468     | 78115      | 3712000000   |
# | Angola      | Africa    | 1246700 | 20609294   | 100990000000 |
# +-------------+-----------+---------+------------+--------------+
# Output: 
# +-------------+------------+---------+
# | name        | population | area    |
# +-------------+------------+---------+
# | Afghanistan | 25500100   | 652230  |
# | Algeria     | 37100000   | 2381741 |
# +-------------+------------+---------+

SELECT name, population, area FROM World WHERE population > 24999999 OR area >= 3000000;

# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | product_id  | int     |
# | low_fats    | enum    |
# | recyclable  | enum    |
# +-------------+---------+
# product_id is the primary key for this table.
# low_fats is an ENUM of type ('Y', 'N') where 'Y' means this product is low fat and 'N' means it is not.
# recyclable is an ENUM of types ('Y', 'N') where 'Y' means this product is recyclable and 'N' means it is not.
# Write an SQL query to find the ids of products that are both low fat and recyclable.
# Return the result table in any order.
# The query result format is in the following example.
# Example 1:
# Input: 
# Products table:
# +-------------+----------+------------+
# | product_id  | low_fats | recyclable |
# +-------------+----------+------------+
# | 0           | Y        | N          |
# | 1           | Y        | Y          |
# | 2           | N        | Y          |
# | 3           | Y        | Y          |
# | 4           | N        | N          |
# +-------------+----------+------------+
# Output: 
# +-------------+
# | product_id  |
# +-------------+
# | 1           |
# | 3           |
# +-------------+
# Explanation: Only products 1 and 3 are both low fat and recyclable.

SELECT product_id FROM Products 
WHERE low_fats = 'Y' AND recyclable = 'Y';

# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | id          | int     |
# | name        | varchar |
# | referee_id  | int     |
# +-------------+---------+
# id is the primary key column for this table.
# Each row of this table indicates the id of a customer, their name, and the id of the customer who referred them.
# Write an SQL query to report the names of the customer that are not referred by the customer with id = 2.
# Return the result table in any order.
# The query result format is in the following example.
# Example 1:
# Input: 
# Customer table:
# +----+------+------------+
# | id | name | referee_id |
# +----+------+------------+
# | 1  | Will | null       |
# | 2  | Jane | null       |
# | 3  | Alex | 2          |
# | 4  | Bill | null       |
# | 5  | Zack | 1          |
# | 6  | Mark | 2          |
# +----+------+------------+
# Output: 
# +------+
# | name |
# +------+
# | Will |
# | Jane |
# | Bill |
# | Zack |
# +------+

SELECT name FROM Customer
WHERE
referee_id != 2 OR referee_id is NULL;

# Table: Customers
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | id          | int     |
# | name        | varchar |
# +-------------+---------+
# id is the primary key column for this table.
# Each row of this table indicates the ID and name of a customer.
# Table: Orders
# +------------+------+
# | Column Name | Type |
# +-------------+------+
# | id          | int  |
# | customerId  | int  |
# +-------------+------+
# id is the primary key column for this table.
# customerId is a foreign key of the ID from the Customers table.
# Each row of this table indicates the ID of an order and the ID of the customer who ordered it.
# Write an SQL query to report all customers who never order anything.
# Return the result table in any order.
# The query result format is in the following example.
# Example 1:
# Input: 
# Customers table:
# +----+-------+
# | id | name  |
# +----+-------+
# | 1  | Joe   |
# | 2  | Henry |
# | 3  | Sam   |
# | 4  | Max   |
# +----+-------+
# Orders table:
# +----+------------+
# | id | customerId |
# +----+------------+
# | 1  | 3          |
# | 2  | 1          |
# +----+------------+
# Output: 
# +-----------+
# | Customers |
# +-----------+
# | Henry     |
# | Max       |
# +-----------+

SELECT name as Customers
FROM customers
LEFT JOIN orders
ON customers.id = orders.customerId
WHERE orders.id IS NULL;

# Table: Employees
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | employee_id | int     |
# | name        | varchar |
# | salary      | int     |
# +-------------+---------+
# employee_id is the primary key for this table.
# Each row of this table indicates the employee ID, employee name, and salary.
# Write an SQL query to calculate the bonus of each employee. The bonus of an employee is 100% of their salary if the ID of the employee is an odd number and the employee name does not start with the character 'M'. The bonus of an employee is 0 otherwise.
# Return the result table ordered by employee_id.
# The query result format is in the following example.
# Example 1:
# Input: 
# Employees table:
# +-------------+---------+--------+
# | employee_id | name    | salary |
# +-------------+---------+--------+
# | 2           | Meir    | 3000   |
# | 3           | Michael | 3800   |
# | 7           | Addilyn | 7400   |
# | 8           | Juan    | 6100   |
# | 9           | Kannon  | 7700   |
# +-------------+---------+--------+
# Output: 
# +-------------+-------+
# | employee_id | bonus |
# +-------------+-------+
# | 2           | 0     |
# | 3           | 0     |
# | 7           | 7400  |
# | 8           | 0     |
# | 9           | 7700  |
# +-------------+-------+
# Explanation: 
# The employees with IDs 2 and 8 get 0 bonus because they have an even employee_id.
# The employee with ID 3 gets 0 bonus because their name starts with 'M'.
# The rest of the employees get a 100% bonus.

SELECT employee_id,
CASE
WHEN employee_id % 2 = 1 AND name NOT LIKE 'M%' THEN salary
ELSE 0
END AS bonus
FROM Employees
ORDER BY employee_id;

# Table: Salary
# +-------------+----------+
# | Column Name | Type     |
# +-------------+----------+
# | id          | int      |
# | name        | varchar  |
# | sex         | ENUM     |
# | salary      | int      |
# +-------------+----------+
# id is the primary key for this table.
# The sex column is ENUM value of type ('m', 'f').
# The table contains information about an employee.
# Write an SQL query to swap all 'f' and 'm' values (i.e., change all 'f' values to 'm' and vice versa) with a single update statement and no intermediate temporary tables.
# Note that you must write a single update statement, do not write any select statement for this problem.
# The query result format is in the following example.
# Example 1:
# Input: 
# Salary table:
# +----+------+-----+--------+
# | id | name | sex | salary |
# +----+------+-----+--------+
# | 1  | A    | m   | 2500   |
# | 2  | B    | f   | 1500   |
# | 3  | C    | m   | 5500   |
# | 4  | D    | f   | 500    |
# +----+------+-----+--------+
# Output: 
# +----+------+-----+--------+
# | id | name | sex | salary |
# +----+------+-----+--------+
# | 1  | A    | f   | 2500   |
# | 2  | B    | m   | 1500   |
# | 3  | C    | f   | 5500   |
# | 4  | D    | m   | 500    |
# +----+------+-----+--------+
# Explanation: 
# (1, A) and (3, C) were changed from 'm' to 'f'.
# (2, B) and (4, D) were changed from 'f' to 'm'.

UPDATE Salary
SET sex =
CASE WHEN sex = 'm' THEN 'f'
ELSE 'm'
END;