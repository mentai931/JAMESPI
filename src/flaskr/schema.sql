PRAGMA foreign_keys = ON;


CREATE TABLE BoxData (
        TC_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Temperature REAL NOT NULL,
        Humidity REAL NOT NULL,
        Datum TIMESTAMP NOT NULL
);

