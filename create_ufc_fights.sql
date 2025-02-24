-- Create a table, ufc_fights, in database ufc_scorigami.db
CREATE TABLE ufc_fights (
    event TEXT,
    fighter_1 TEXT,
    fighter_2 TEXT,
    result TEXT,
    method TEXT,
    round INT,
    time TEXT
);
-- Import data from ufcfights.csv into ufc_fights
.mode csv
.import ufcfights.csv ufc_fights

-- Delete the first row of the table
DELETE FROM ufc_fights WHERE event = 'event';

-- Gather data on all the different methods of winning a fight
SELECT DISTINCT method FROM ufc_fights;
SELECT method, COUNT(*) AS count
FROM ufc_fights
GROUP BY method
ORDER BY count DESC;

-- Refine ufc_fights for only what's needed
CREATE TABLE refined_ufc_fights AS
SELECT method, round, time
FROM ufc_fights;
DROP TABLE ufc_fights;
ALTER TABLE refined_ufc_fights RENAME to ufc_fights;

-- Refine ufc_fights for only fights that are 5 rounds or less and 5 minutes or less
CREATE TABLE cleaned_ufc_fights AS
SELECT *
FROM ufc_fights
WHERE (round BETWEEN 1 AND 5)
AND (
    CAST(SUBSTR(time, 1, INSTR(time, ':') - 1) AS INTEGER) * 60 
    + CAST(SUBSTR(time, INSTR(time, ':') + 1) AS INTEGER) 
    <= 300
);
DROP TABLE ufc_fights;
ALTER TABLE cleaned_ufc_fights RENAME TO ufc_fights;