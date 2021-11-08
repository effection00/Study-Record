"""
Part 3

각 질문에서 명시한 요구사항을 충족하는 SQL 문을 작성합니다.
"""

QUERY_1 = "SELECT c.CustomerId,\
UPPER(c.City) || ' ' || UPPER(c.Country) AS 'CITY_COUNTRY'\
FROM customers c"

QUERY_2 = "SELECT LOWER(SUBSTR(c.FirstName,1,4)  || '' || SUBSTR(c.LastName,1,2)) \
AS change_name \
FROM customers c"

QUERY_3 = "SELECT employeeid \
FROM (SELECT e.EmployeeId, e.LastName \
FROM employees e \
WHERE '2013-01-01' > e.HireDate \
ORDER BY 2)"

QUERY_4 = "SELECT  c.FirstName || '' || c.LastName || '' || i.InvoiceId AS 'CITY_COUNTRY' \
FROM customers c  \
JOIN invoices i \
ON c.CustomerId = i.CustomerId \
ORDER BY c.FirstName, c.LastName,  i.InvoiceId"

QUERY_5 = "SELECT new.Name \
FROM (SELECT * \
FROM albums a \
JOIN tracks t \
ON a.AlbumId  = t.AlbumId \
WHERE a.Title ='Unplugged' OR a.Title = 'Outbreak') as new;"

