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