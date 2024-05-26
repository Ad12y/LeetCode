# Write your MySQL query statement below
Select request_at as Day, ROUND(avg(Final),2) as 'Cancellation Rate' FROM (
select request_at,
Case
    WHEN status != 'completed' AND banned_clients = 'No' AND banned_drivers = 'No'
    THEN 1
    WHEN banned_clients = 'No' AND banned_drivers = 'No'
    THEN 0
    ELSE NULL
END as Final
FROM (Select status, request_at, banned_clients, U.banned as banned_drivers from (Select driver_id, status, request_at, banned as banned_clients from Trips T left join Users U on T.client_id = U.users_id) as D left join Users U on U.users_id = D.driver_id where request_at <= '2013-10-03' and request_at >= '2013-10-01') as temp) as temp2 where Final is not NULL group by Day