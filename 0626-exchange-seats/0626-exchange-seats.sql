# Write your MySQL query statement below
SELECT id, CASE
  WHEN id % 2 = 0 THEN even
  ELSE
    CASE
    WHEN odd is NULL THEN student
    ELSE odd
    END
  END as student 
  from (SELECT id, student, LAG(student,1) over() AS even, LEAD(student,1) over() AS odd from Seat) as y