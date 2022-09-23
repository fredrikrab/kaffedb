BEGIN TRANSACTION;
PRAGMA foreign_keys=ON;

CREATE TABLE users(
    user_email VARCHAR(255)         PRIMARY KEY,
    password VARCHAR(255)           NOT NULL,
    user_name VARCHAR(255)          NOT NULL,
    user_country VARCHAR(255)       NOT NULL
);

CREATE TABLE coffee(
    coffee_id INTEGER               PRIMARY KEY,
    coffee_name VARCHAR(255)        NOT NULL,
    coffee_description TEXT         NOT NULL,
    kilo_price_nok REAL             NOT NULL,
    roast_degree VARCHAR(7)         CHECK(roast_degree IN('mørk', 'middels', 'lys')),
    roast_date DATE                 NOT NULL,
    roastery_name VARCHAR(255)      NOT NULL,
    FOREIGN KEY (roastery_name)     REFERENCES roasteries(roastery_name)
                                    ON UPDATE CASCADE
                                    ON DELETE RESTRICT,
    UNIQUE (coffee_name, roastery_name)
);

CREATE TABLE reviews(
    review_id INTEGER               PRIMARY KEY,
    user_email VARCHAR(255)         NOT NULL,
    coffee_id INTEGER               NOT NULL,
    date_time DATE                  NOT NULL,
    rating INTEGER                  CHECK(rating BETWEEN 0 AND 10),
    note TEXT,
    FOREIGN KEY (user_email)        REFERENCES users(user_email)
                                    ON UPDATE CASCADE
                                    ON DELETE CASCADE,
    FOREIGN KEY (coffee_id)         REFERENCES coffee(coffee_id)
                                    ON DELETE RESTRICT,
    UNIQUE(user_email, coffee_id, date_time)
);

CREATE TABLE roasteries(
    roastery_name VARCHAR(255)      PRIMARY KEY
);

CREATE TABLE farms(
    farm_name VARCHAR(255)          PRIMARY KEY,
    elevation INTEGER               CHECK(elevation >= 0),
    farm_country VARCHAR(255)       NOT NULL,
    region VARCHAR(255)             NOT NULL
);

CREATE TABLE refinement_methods(
    refinement_name VARCHAR(255)    PRIMARY KEY,
    refinement_description TEXT     NOT NULL
); 

CREATE TABLE batches(
    batch_id INTEGER                PRIMARY KEY,
    coffee_id INTEGER               NOT NULL,
    roastery_name VARCHAR(255)      NOT NULL,
    farm_name VARCHAR(255)          NOT NULL,
    refinement_name VARCHAR(255)    NOT NULL,
    harvest_year INTEGER            NOT NULL,
    kilo_price_usd REAL             NOT NULL,
    FOREIGN KEY (coffee_id)         REFERENCES coffee(coffee_id)
                                    ON DELETE CASCADE,
    FOREIGN KEY (farm_name)         REFERENCES farms(farm_name)
                                    ON UPDATE CASCADE
                                    ON DELETE RESTRICT,
    FOREIGN KEY (roastery_name)     REFERENCES roasteries(roastery_name)
                                    ON UPDATE CASCADE
                                    ON DELETE RESTRICT,
    FOREIGN KEY (refinement_name)   REFERENCES refinement_methods(refinement_name)
                                    ON UPDATE CASCADE
                                    ON DELETE RESTRICT,
    UNIQUE(coffee_id)
);

CREATE TABLE coffee_beans(
    bean_type VARCHAR(8)            PRIMARY KEY
                                    CHECK(bean_type IN ('arabica', 'robusta', 'liberica'))
);

CREATE TABLE beans_in_batch(
    batch_id INTEGER                NOT NULL,
    bean_type VARCHAR(8)            NOT NULL,
    FOREIGN KEY (batch_id)          REFERENCES batches(batch_id)
                                    ON DELETE CASCADE,
    FOREIGN KEY (bean_type)         REFERENCES coffee_beans(bean_type)
                                    ON UPDATE CASCADE
                                    ON DELETE RESTRICT,
    PRIMARY KEY(batch_id, bean_type)
);

CREATE TABLE farm_cultivate_beans(
    farm_name VARCHAR(255)          NOT NULL,
    bean_type VARCHAR(8)            NOT NULL,
    FOREIGN KEY (farm_name)         REFERENCES farms(farm_name)
                                    ON UPDATE CASCADE
                                    ON DELETE CASCADE,
    FOREIGN KEY (bean_type)         REFERENCES coffee_beans(bean_type)
                                    ON UPDATE CASCADE
                                    ON DELETE CASCADE,
    PRIMARY KEY(farm_name, bean_type)
);

COMMIT;