-- Question: List employees first name, last name, job if, salary ,department name and manager_id of that department for those who work as SA_REP or SA_MAN

-- Something else
SELECT e.first_name, e.last_name, e.salary, jg.grade_level
FROM hr_employees e JOIN hr_job_grades jg
on e.salary  between jg.lowest_sal and jg.highest_sal


-- Who makes more than Average Salary?
-- Dynamic Subquery
SELECT * FROM hr_employees WHERE salary > (SELECT avg(salary) FROM HR_EMPLOYEES)


-- Dynamic Subquery
-- Job code may change so using this as a subquery is more feasible
SELECT * FROM HR_EMPLOYEES WHERE job_id = (
    SELECT job_id from HR_EMPLOYEES WHERE last_name='Abel' and first_name='Ellen') 
    AND salary > (SELECT salary from HR_EMPLOYEES WHERE last_name='Abel' and first_name='Ellen') ;