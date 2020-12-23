BEGIN;

CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL, 
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

-- Running upgrade  -> aea4a7edf3c4

CREATE TABLE measurements (
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

INSERT INTO alembic_version (version_num) VALUES ('aea4a7edf3c4');

COMMIT;

