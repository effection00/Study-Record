"""
Part 2

각 질문에서 명시한 요구사항을 충족하는 SQL 문을 작성합니다.
"""

QUERY_1 = "SELECT a.Title FROM albums a \
WHERE a.AlbumId=31;"

QUERY_2 = "SELECT AlbumId \
FROM albums a \
JOIN artists a2 \
ON a.ArtistId = a2.ArtistId \
WHERE a2.Name LIKE '%the%';"

QUERY_3 = "SELECT i.InvoiceId \
FROM invoices i \
WHERE i.BillingCity='Stuttgart' OR i.BillingCity='Oslo' OR i.BillingCity='Redmond'\
ORDER BY 1;"

QUERY_4 = "SELECT t.TrackId \
FROM tracks t \
WHERE t.Name LIKE 'The%';"

QUERY_5 = "SELECT c.CustomerId \
FROM customers c \
WHERE Email LIKE '%gmail.com';"

QUERY_6 = "SELECT i.InvoiceId \
FROM invoices i \
WHERE (i.CustomerId=29 OR i.CustomerId=30 OR i.CustomerId=63) \
AND i.Total >= 1 AND i.Total <= 3;"

QUERY_7 = "SELECT t.TrackId \
FROM genres g \
JOIN tracks t \
ON g.GenreId = t.GenreId \
WHERE g.Name = 'Soundtrack' \
AND t.Milliseconds >= 300000 AND t.Milliseconds <= 400000;"

QUERY_8 = "SELECT count(*) \
FROM customers c \
GROUP BY c.Country;"

QUERY_9 = "SELECT CustomerId  \
FROM(SELECT i.CustomerId, sum(i.Total) \
FROM invoices i \
GROUP BY i.CustomerId \
ORDER BY 2 DESC \
LIMIT 5);"


QUERY_10 = "SELECT g.Name AS genre_name ,count(DISTINCT CustomerId) AS The_Number_of_customer_ID \
FROM(SELECT * \
FROM (SELECT * \
FROM invoice_items ii \
JOIN tracks t \
ON ii.TrackId = t.TrackId ) AS M \
JOIN invoices i \
ON M.InvoiceId =i.InvoiceId) AS E \
JOIN genres g \
ON E.GenreID = g.GenreId \
GROUP BY g.Name;"

