/* This will hold the foundation for our database. Creating the schema for the tables used
for the rest of the project */

DROP TABLE IF EXISTS spells;

CREATE TABLE spells (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  spellname TEXT UNIQUE NOT NULL,
  type TEXT NOT NULL,
  notes TEXT NOT NULL
);
