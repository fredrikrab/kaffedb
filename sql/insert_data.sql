-- BRUKERHISTORIE 1

INSERT INTO users (user_email, password, user_name, user_country)
VALUES ('epost@server.no', 'passord123', 'Jens', 'Norge');

INSERT INTO farms (farm_name, elevation, farm_country, region)
VALUES ('Nombre de Dios', 1500, 'El Salvador', 'Santa Ana');

INSERT INTO roasteries (roastery_name)
VALUES ('Jacobsen & Svart');

INSERT INTO coffee (coffee_id, coffee_name, coffee_description, kilo_price_nok, roast_degree, roast_date, roastery_name)
VALUES (null, 'Vinterkaffe 2022', 'En velsmakende og kompleks kaffe for mørketiden', 600, 'lys', '2022-01-20', 'Jacobsen & Svart');

INSERT INTO refinement_methods
VALUES ('Bærtørket', 'Bourbon');

INSERT INTO batches
VALUES (null, 1, 'Jacobsen & Svart', 'Nombre de Dios', 'Bærtørket', 2021, 8);

INSERT INTO reviews (review_id, user_email, coffee_id, date_time, rating, note)
VALUES(null, 'epost@server.no', (SELECT coffee_id FROM coffee WHERE coffee_name == 'Vinterkaffe 2022'), datetime('now'), 10, 'Wow - en odyss ́e for smaksløkene: sitrusskall, melkesjokolade, aprikos!');

-- BRUKERHISTORIE 2

INSERT INTO users (user_email, password, user_name, user_country)
VALUES ('hanna@gmail.com', 'passord123', 'Hanna', 'Norge');

INSERT INTO users (user_email, password, user_name, user_country)
VALUES ('jens@gmail.com', 'passord123', 'Jens', 'Norge');

INSERT INTO reviews (review_id, user_email, coffee_id, date_time, rating, note)
VALUES(null, 'jens@gmail.com', (SELECT coffee_id FROM coffee WHERE coffee_name == 'Vinterkaffe 2022'), datetime('now', '+1 hours'), 8, 'Notat!');


-- BRUKERHISTORIE 3

INSERT INTO roasteries (roastery_name) VALUES ('Kafeteros');
INSERT INTO roasteries (roastery_name) VALUES ('Maridalen Brenneri');
INSERT INTO roasteries (roastery_name) VALUES ('Radikal Roasters');

INSERT INTO coffee (coffee_id, coffee_name, coffee_description, kilo_price_nok, roast_degree, roast_date, roastery_name)
VALUES (null, 'Ali kaffe', 'Beskrivelse', 800, 'lys', '2022-01-20', 'Maridalen Brenneri');
INSERT INTO coffee (coffee_id, coffee_name, coffee_description, kilo_price_nok, roast_degree, roast_date, roastery_name)
VALUES (null, 'Morgenkaffe', 'Beskrivelse', 350, 'lys', '2022-01-20', 'Kafeteros');
INSERT INTO coffee (coffee_id, coffee_name, coffee_description, kilo_price_nok, roast_degree, roast_date, roastery_name)
VALUES (null, 'Luksuskaffe', 'Beskrivelse', 1000, 'lys', '2022-01-20', 'Radikal Roasters');

INSERT INTO reviews (review_id, user_email, coffee_id, date_time, rating, note)
VALUES(null, 'hanna@gmail.com', (SELECT coffee_id FROM coffee WHERE coffee_name == 'Morgenkaffe'), datetime('now', '+1 days'), 2, 'Notat');
INSERT INTO reviews (review_id, user_email, coffee_id, date_time, rating, note)
VALUES(null, 'hanna@gmail.com', (SELECT coffee_id FROM coffee WHERE coffee_name == 'Ali kaffe'), datetime('now', '+2 days'), 10, 'Notat');
INSERT INTO reviews (review_id, user_email, coffee_id, date_time, rating, note)
VALUES(null, 'hanna@gmail.com', (SELECT coffee_id FROM coffee WHERE coffee_name == 'Vinterkaffe 2022'), datetime('now', '+3 days'), 6, 'Notat');
INSERT INTO reviews (review_id, user_email, coffee_id, date_time, rating, note)
VALUES(null, 'hanna@gmail.com', (SELECT coffee_id FROM coffee WHERE coffee_name == 'Ali kaffe'), datetime('now','start of year', '-1 months'), 6, 'Notat');

INSERT INTO reviews (review_id, user_email, coffee_id, date_time, rating, note)
VALUES(null, 'epost@server.no', (SELECT coffee_id FROM coffee WHERE coffee_name == 'Morgenkaffe'), datetime('now', '+4 days'), 7, 'Notat');
INSERT INTO reviews (review_id, user_email, coffee_id, date_time, rating, note)
VALUES(null, 'epost@server.no', (SELECT coffee_id FROM coffee WHERE coffee_name == 'Ali kaffe'), datetime('now', '+5 days'), 8, 'Notat');
INSERT INTO reviews (review_id, user_email, coffee_id, date_time, rating, note)
VALUES(null, 'epost@server.no', (SELECT coffee_id FROM coffee WHERE coffee_name == 'Vinterkaffe 2022'), datetime('now', '+10 days'), 4, 'Notat');
INSERT INTO reviews (review_id, user_email, coffee_id, date_time, rating, note)
VALUES(null, 'epost@server.no', (SELECT coffee_id FROM coffee WHERE coffee_name == 'Luksuskaffe'), datetime('now', '+6 days'), 9, 'Notat');
INSERT INTO reviews (review_id, user_email, coffee_id, date_time, rating, note)
VALUES(null, 'epost@server.no', (SELECT coffee_id FROM coffee WHERE coffee_name == 'Ali kaffe'), datetime('now', '-2 days'), 1, 'Notat');

-- BRUKERHISTORIE 4

INSERT INTO reviews (review_id, user_email, coffee_id, date_time, rating, note)
VALUES(null, 'epost@server.no', (SELECT coffee_id FROM coffee WHERE coffee_name == 'Ali kaffe'), datetime('now', '-4 months'), 6, 'Mer floral kaffe skal man lete lenge etter!');

INSERT INTO coffee (coffee_id, coffee_name, coffee_description, kilo_price_nok, roast_degree, roast_date, roastery_name)
VALUES (null, 'Blomsterkaffe', 'For deg som vil ha floral kaffe', 1000, 'lys', '2022-01-20', 'Radikal Roasters');

-- BRUKERHISTORIE 5 '

INSERT INTO farms (farm_name, elevation, farm_country, region)
VALUES ('Rwanda de Dios', 2500, 'Rwanda', 'Øst');

INSERT INTO farms (farm_name, elevation, farm_country, region)
VALUES ('Colombia de Dios', 3500, 'Colombia', 'Nord');

INSERT INTO refinement_methods
VALUES ('Vasket', 'Bourbon');

INSERT INTO coffee (coffee_id, coffee_name, coffee_description, kilo_price_nok, roast_degree, roast_date, roastery_name)
VALUES (null, 'Rwanda kaffe 1', 'For deg som vil ha floral kaffe', 1000, 'lys', '2022-01-20', 'Rwanda International');

INSERT INTO coffee (coffee_id, coffee_name, coffee_description, kilo_price_nok, roast_degree, roast_date, roastery_name)
VALUES (null, 'Rwanda kaffe 2', 'For deg som vil ha floral kaffe', 1000, 'lys', '2022-01-20', 'Rwanda International');

INSERT INTO coffee (coffee_id, coffee_name, coffee_description, kilo_price_nok, roast_degree, roast_date, roastery_name)
VALUES (null, 'Rwanda kaffe 3', 'For deg som vil ha floral kaffe', 1000, 'lys', '2022-01-20', 'Rwanda International');

INSERT INTO coffee (coffee_id, coffee_name, coffee_description, kilo_price_nok, roast_degree, roast_date, roastery_name)
VALUES (null, 'Colombia kaffe 1', 'For deg som vil ha floral kaffe', 1000, 'lys', '2022-01-20', 'Colombia International');

INSERT INTO coffee (coffee_id, coffee_name, coffee_description, kilo_price_nok, roast_degree, roast_date, roastery_name)
VALUES (null, 'Colombia kaffe 2', 'For deg som vil ha floral kaffe', 1000, 'lys', '2022-01-20', 'Colombia International');

INSERT INTO batches (batch_id, coffee_id, roastery_name, farm_name, refinement_name, harvest_year, kilo_price_usd)
VALUES (null, (SELECT coffee_id FROM coffee WHERE coffee_name == 'Rwanda kaffe 1'), 'Rwanda International', 'Rwanda de Dios', 'Vasket', 2011, 4);

INSERT INTO batches (batch_id, coffee_id, roastery_name, farm_name, refinement_name, harvest_year, kilo_price_usd)
VALUES (null, (SELECT coffee_id FROM coffee WHERE coffee_name == 'Rwanda kaffe 2'), 'Rwanda International', 'Rwanda de Dios', 'Bærtørket', 2012, 4);

INSERT INTO batches (batch_id, coffee_id, roastery_name, farm_name, refinement_name, harvest_year, kilo_price_usd)
VALUES (null, (SELECT coffee_id FROM coffee WHERE coffee_name == 'Rwanda kaffe 3'), 'Rwanda International', 'Rwanda de Dios', 'Bærtørket', 2012, 4);

INSERT INTO batches (batch_id, coffee_id, roastery_name, farm_name, refinement_name, harvest_year, kilo_price_usd)
VALUES (null, (SELECT coffee_id FROM coffee WHERE coffee_name == 'Colombia kaffe 1'), 'Colombia International', 'Colombia de Dios', 'Vasket', 1911, 4);

INSERT INTO batches (batch_id, coffee_id, roastery_name, farm_name, refinement_name, harvest_year, kilo_price_usd)
VALUES (null, (SELECT coffee_id FROM coffee WHERE coffee_name == 'Colombia kaffe 2'), 'Colombia International', 'Colombia de Dios', 'Bærtørket', 1912, 4);

-- DIVERSE

INSERT INTO coffee_beans VALUES('arabica');
INSERT INTO coffee_beans VALUES('robusta');
INSERT INTO coffee_beans VALUES('liberica');