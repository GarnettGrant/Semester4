--1. Which customers live in New Jersey? List each customer’s last name, first name, and state.
SELECT LASTNAME,FIRSTNAME,STATE FROM JL_CUSTOMERS WHERE STATE = 'NJ'
--2. Which orders shipped after April 1, 2009? List each order number and the date it shipped.
SELECT ORDER#,SHIPDATE FROM JL_ORDERS WHERE ORDERDATE > ('09-04-01')

--3. Which books aren’t in the Fitness category? List each book title and category.
SELECT TITLE,CATEGORY FROM JL_BOOKS WHERE CATEGORY <> 'FITNESS'

--4. Which customers live in Georgia or New Jersey? Put the results in ascending order by last name. List 
--each customer’s customer number, last name, and state. Write this query in two different ways.
SELECT * FROM JL_ORDERS WHERE SHIPSTATE = 'NJ' OR SHIPSTATE = 'GA'

--5. Which orders were placed on or before April 1, 2009? List each order number and order date. Write 
--this query in two different ways.
SELECT ORDER#,ORDERDATE FROM JL_ORDERS WHERE ORDERDATE <= ('09-04-01')
SELECT ORDER#,ORDERDATE FROM JL_ORDERS WHERE ORDERDATE < ('09-04-01') OR ORDERDATE = ('09-04-01')

--6. List all authors whose last name contains the letter pattern “IN.” Put the results in order of last name, 
--then first name. List each author’s last name and first name.
SELECT * FROM JL_AUTHOR WHERE LNAME LIKE '%IN%' ORDER BY LNAME,FNAME

--7. List all customers who were referred to the bookstore by another customer. List each customer’s last 
--name and the number of the customer who made the referral.
SELECT LASTNAME,CUSTOMER# FROM JL_CUSTOMERS WHERE REFERRED is NOT NULL


--8. Display the book title and category for all books in the Children and Cooking categories. Create three 
--different queries to accomplish this task:
SELECT TITLE,CATEGORY FROM JL_BOOKS WHERE CATEGORY LIKE '%CHILD%'
SELECT TITLE,CATEGORY FROM JL_BOOKS WHERE CATEGORY = 'CHILDREN'
SELECT 'Title: '|| TITLE || ' | ' || 'Category: ' || CATEGORY as "Title, Category" FROM JL_BOOKS WHERE CATEGORY LIKE '%CHILD%'