-- Logical schema matching the questionnaire's entities.
CREATE TABLE state (id INTEGER PRIMARY KEY, name VARCHAR(100) NOT NULL);
CREATE TABLE lga (uniqueid INTEGER PRIMARY KEY, lga_name VARCHAR(150) NOT NULL, state_id INTEGER NOT NULL REFERENCES state(id));
CREATE TABLE ward (uniqueid INTEGER PRIMARY KEY, ward_name VARCHAR(150) NOT NULL, lga_id INTEGER NOT NULL REFERENCES lga(uniqueid));
CREATE TABLE polling_unit (uniqueid INTEGER PRIMARY KEY, polling_unit_name VARCHAR(255) NOT NULL, ward_id INTEGER NOT NULL REFERENCES ward(uniqueid), lga_id INTEGER NOT NULL REFERENCES lga(uniqueid), state_id INTEGER NOT NULL REFERENCES state(id));
CREATE TABLE polling_unit_result (id SERIAL PRIMARY KEY, polling_unit_id INTEGER NOT NULL REFERENCES polling_unit(uniqueid), party VARCHAR(20) NOT NULL, score INTEGER NOT NULL DEFAULT 0, UNIQUE(polling_unit_id,party));
