--all these practices are from JL_XXXX tables
SELECT * FROM JL_BOOKS

--Practice 1: Determine how many books are in the Cooking category.
SELECT COUNT(*) as "# of Cooking Books" FROM JL_BOOKS 
WHERE CATEGORY = 'COOKING'

-- practice#2: List how many books are in each category
SELECT CATEGORY, COUNT(*) as "Book Count" FROM JL_BOOKS
GROUP BY CATEGORY
ORDER BY CATEGORY

--practice #3: . List the retail price of the least expensive book in the Computer category
SELECT TITLE, retail FROM JL_BOOKS
WHERE retail = (SELECT MIN(RETAIL) FROM JL_BOOKS)

--practice #4: Display the number of books with a retail price of more than $30.00.
SELECT COUNT(*) as "# of Book's over $30.00" from JL_BOOKS
where retail > 30