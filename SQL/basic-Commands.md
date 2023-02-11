/*Erzeugt eine Liste mit 3 Spalten ( ID,Name, Geburtstag) */

CREATE TABLE friends (
   id INTEGER,
   name TEXT,
   birthday DATE
);
/*Gewünschte Spalten werden angewählt*/
INSERT INTO friends (id, name, birthday) 
/*Befüllen der Tabellle mit Inhalt*/
VALUES (1, 'Ororo Munroe', '1940-05-30'); /*ID = 1, Name = 'Ororo Munroe', Geburtstag = 1940-05-30 */
INSERT INTO friends (id, name, birthday) 
VALUES (2,'Hans','1999-10-12');
INSERT INTO friends (id, name, birthday) 
VALUES (3,'Klaus','1998-11-10');


/*Ändern eines Inhalts innerhalb der angelegten Tabelle*/
UPDATE friends              
SET name = 'Storm'
WHERE id = 1;

/*Ändern der Tabelle (Spalte Email wird angelegt) */
ALTER TABLE friends
ADD COLUMN email TEXT;

UPDATE friends 
set email = 'storm@codecademy.com'
WHERE id = 1;
/*Löschen von einer Zelle*/
DELETE FROM friends
WHERE id = 1;

SELECT * FROM friends