SELECT 
    request_at AS Day, 
    ROUND(AVG(Final), 2) AS 'Cancellation Rate'
FROM (
    SELECT 
        request_at,
        CASE
            WHEN status != 'completed' AND banned_clients = 'No' AND banned_drivers = 'No' THEN 1
            WHEN banned_clients = 'No' AND banned_drivers = 'No' THEN 0
            ELSE NULL
        END AS Final
    FROM (
        SELECT 
            status, 
            request_at, 
            banned_clients, 
            U.banned AS banned_drivers 
        FROM (
            SELECT 
                driver_id, 
                status, 
                request_at, 
                banned AS banned_clients 
            FROM Trips T 
            LEFT JOIN Users U ON T.client_id = U.users_id
        ) AS D 
        LEFT JOIN Users U ON U.users_id = D.driver_id 
        WHERE request_at <= '2013-10-03' AND request_at >= '2013-10-01'
    ) AS temp
) AS temp2 
WHERE Final IS NOT NULL 
GROUP BY Day;
