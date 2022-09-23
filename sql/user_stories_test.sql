-- Brukerhistorie 2
SELECT user_name, count(*)
FROM (
         SELECT DISTINCT user_email, coffee_id
         FROM reviews
         WHERE date_time >= datetime('now', 'start of year')
     )
JOIN users USING(user_email)
GROUP BY user_email
ORDER BY count(*) DESC;

-- Brukerhistorie 3
SELECT roastery_name, coffee_name, kilo_price_nok, AVG(rating)
FROM (SELECT rating, coffee_id FROM reviews)
JOIN coffee USING(coffee_id)
GROUP BY coffee_id
ORDER BY AVG(rating)/kilo_price_nok DESC;


-- Brukerhistorie 4
SELECT roastery_name, coffee_name
FROM (  SELECT coffee_id FROM reviews
        WHERE note LIKE '%floral%'  )
JOIN coffee USING(coffee_id)
UNION
SELECT roastery_name, coffee_name FROM coffee
WHERE coffee_description LIKE '%floral%';

-- Brukerhistorie 5
SELECT roastery_name, coffee_name
FROM (
        SELECT farm_name FROM farms
        WHERE farm_country IN ('Rwanda', 'Colombia')
    ), (
        SELECT refinement_name FROM refinement_methods
        WHERE refinement_name != 'Vasket'
    )
NATURAL JOIN batches
NATURAL JOIN coffee;

-- Print info about a table
PRAGMA table_info('beans_in_batch')