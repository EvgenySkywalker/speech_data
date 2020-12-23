BEGIN;

CREATE TABLE measurements_7 (
    id SERIAL NOT NULL, 
    user_id INTEGER NOT NULL, 
    words JSON NOT NULL, 
    said_words JSON NOT NULL, 
    timings JSON NOT NULL, 
    accuracy FLOAT NOT NULL, 
    wps FLOAT NOT NULL, 
    sps FLOAT NOT NULL, 
    PRIMARY KEY (id)
);

COMMIT;

