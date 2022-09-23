BEGIN TRANSACTION;

-- USERS
INSERT INTO users (user_email,password,user_name, user_country) VALUES ("bruker1@ntnu.no", "passord1", "Bruker", "Norge");
INSERT INTO users (user_email,password,user_name, user_country) VALUES ("bruker2@tele2.no", "passord2", "Brukeren", "Danmark");
INSERT INTO users (user_email,password,user_name, user_country) VALUES ("bruker3@hotmail.com", "passord1", "Bruker", "England");
INSERT INTO users (user_email,password,user_name, user_country) VALUES ("bruker1@tele2.no", "passord1", "Jens", "Tyskland");
INSERT INTO users (user_email,password,user_name, user_country) VALUES ("bruker1@mail.com", "passord1", "Hanna", "Kina");
INSERT INTO users (user_email,password,user_name, user_country) VALUES ("super@bruker.no", "123", "Hen", "Norge");

-- farms
INSERT INTO farms (farm_name, elevation, farm_country, region) VALUES ("En gård på Røros", 0, "Norge", "Midt");
INSERT INTO farms (farm_name, elevation, farm_country, region) VALUES ("CockaFarm", 1523, "Colombia", "Sør");
INSERT INTO farms (farm_name, elevation, farm_country, region) VALUES ("BønneGård", 42, "India", "Ikke i India");
INSERT INTO farms (farm_name, elevation, farm_country, region) VALUES ("Blomster", 8520, "WWW", "Alt");

-- bean type


-- farm_cultivate_beans
INSERT INTO farm_cultivate_beans(farm_name, bean_type) VALUES ("CockaFarm", "arabica");
INSERT INTO farm_cultivate_beans(farm_name, bean_type) VALUES ("CockaFarm", "robusta");
INSERT INTO farm_cultivate_beans(farm_name, bean_type) VALUES ("CockaFarm", "liberica");
INSERT INTO farm_cultivate_beans(farm_name, bean_type) VALUES ("En gård på Røros", "liberica");
INSERT INTO farm_cultivate_beans(farm_name, bean_type) VALUES ("En gård på Røros", "arabica");
INSERT INTO farm_cultivate_beans(farm_name, bean_type) VALUES ("Blomster", "arabica");
INSERT INTO farm_cultivate_beans(farm_name, bean_type) VALUES ("Blomster", "robusta");
INSERT INTO farm_cultivate_beans(farm_name, bean_type) VALUES ("BønneGård", "robusta");

-- roasteries
INSERT INTO roasteries (roastery_name) VALUES ("Trondheim Brenneri");
INSERT INTO roasteries (roastery_name) VALUES ("Mongstad Brenneri");
INSERT INTO roasteries (roastery_name) VALUES ("Rætt-i-Kroppen");
INSERT INTO roasteries (roastery_name) VALUES ("coca cola");

-- refinement_methods
INSERT INTO refinement_methods (refinement_name, refinement_description ) VALUES ("Brent","Svart");
INSERT INTO refinement_methods (refinement_name, refinement_description) VALUES ("Vasket","Bløt");
INSERT INTO refinement_methods (refinement_name, refinement_description) VALUES ("Pulverisert","knust");
INSERT INTO refinement_methods (refinement_name, refinement_description) VALUES ("Insta","pulver");
INSERT INTO refinement_methods (refinement_name, refinement_description) VALUES ("Sats","Sats er væsken man lager som skal destilleres. For å lage en sats trenger du 6 til 8 kilo sukker, 1 pakke gjær og vanlig vann. Satsen lager du i ett gjæringskar. De vanligste rommer 30L og det holder perfekt til en sats på 25 liter.");

-- coffee
INSERT INTO coffee (coffee_id, coffee_name, coffee_description, kilo_price_nok, roast_degree, roast_date, roastery_name) VALUES (null, "Karsk", "Stram og god", 100, "lys", datetime('now', '+1 hours'), "Rætt-i-Kroppen");
INSERT INTO coffee (coffee_id, coffee_name, coffee_description, kilo_price_nok, roast_degree, roast_date, roastery_name) VALUES (null, "Friele", "En helt vanlig kaffe", 200, "mørk", datetime('now', '+2 hours'), "Trondheim Brenneri");
INSERT INTO coffee (coffee_id, coffee_name, coffee_description, kilo_price_nok, roast_degree, roast_date, roastery_name) VALUES (null, "Sommerkaffe","En bløt kaffe" , 50, "lys" , datetime('now', '+3 hours'), "Trondheim Brenneri");
INSERT INTO coffee (coffee_id, coffee_name, coffee_description, kilo_price_nok, roast_degree, roast_date, roastery_name) VALUES (null, "Coffee Coke", "Drikkes gjennom nesen", 500, "middels", datetime('now', '+4 hours'), "coca cola");
INSERT INTO coffee (coffee_id, coffee_name, coffee_description, kilo_price_nok, roast_degree, roast_date, roastery_name) VALUES (null, "Oil coffee", "Svart gull", 300, "mørk", datetime('now', '+5 hours'), "Mongstad Brenneri");

-- reviews
INSERT INTO reviews (review_id, user_email, coffee_id, date_time, rating, note) VALUES (null,"bruker1@ntnu.no", 1, datetime('now'), 10, "Var som beskrevet, stram og god! Kjente til og med effekten dagen etter konsumering også!" );
INSERT INTO reviews (review_id, user_email, coffee_id, date_time, rating, note) VALUES (null,"super@bruker.no", 1, datetime('now','-1 hours'), 1, "Fikk en voldsom brennende følelse i halsen slik at jeg kastet opp, æsj!" );
INSERT INTO reviews (review_id, user_email, coffee_id, date_time, rating, note) VALUES (null,"bruker1@tele2.no", 1, datetime('now','-2 hours'), 8, "Ich habe diesen Kaffee geliebt");
INSERT INTO reviews (review_id, user_email, coffee_id, date_time, rating, note) VALUES (null,"bruker1@ntnu.no", 4, datetime('now','+2 hours'), 9, "Rart å drikke kaffe gjennom nesen, men denne kaffen kvikner man til!" );
INSERT INTO reviews (review_id, user_email, coffee_id, date_time, rating, note) VALUES (null,"bruker1@mail.com", 4, datetime('now','+1 hours'), 4, "我更喜欢茶");
INSERT INTO reviews (review_id, user_email, coffee_id, date_time, rating, note) VALUES (null,"bruker1@mail.com", 1, datetime('now','+1 hours'), 7, "几乎和一杯茶一样好");





-- batches
--INSERT INTO batches (batch_id, coffee_id, roastery_name, farm_name, refinement_name, harvest_year, kilo_price_usd) VALUES(1, 1, )



commit transaction;
end transaction;












