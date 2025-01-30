SELECT Students.FirstName, Students.LastName, Students.Email, Orders.OrderID, Orders.OrderDate, Orders.Total 
FROM Students
JOIN Orders
ON Students.StudentID = Orders.CustomerID
WHERE CustomerID=1;