CREATE TABLE ufc_fights (
    event TEXT,
    fighter_1 TEXT,
    fighter_2 TEXT,
    result TEXT,
    method TEXT,
    round INT,
    time TEXT
);
.mode csv
.import ufcfights.csv ufc_fights

DELETE FROM ufc_fights WHERE event = 'event';

SELECT DISTINCT method FROM ufc_fights;
SELECT method, COUNT(*) AS count
FROM ufc_fights
GROUP BY method
ORDER BY count DESC;

CREATE TABLE refined_ufc_fights AS
    SELECT method, round, time
    FROM ufc_fights;

DROP TABLE ufc_fights;
ALTER TABLE refined_ufc_fights RENAME to ufc_fights;