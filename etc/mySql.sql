DROP DATABASE IF EXISTS pet_info;

create database pet_info;

use pet_info;

create table pets  (
    PersonID int NOT NULL AUTO_INCREMENT,
    Name varchar(40),
    Type varchar(40),
    Family varchar(40),
    PRIMARY KEY(PersonID)
);

INSERT INTO pets (Name, Type, Family) VALUES ('Bella', 'Dog', 'Fulton');
INSERT INTO pets (Name, Type, Family) VALUES ('Primrose', 'Cat', 'Fulton');
INSERT INTO pets (Name, Type, Family) VALUES ('Gabriel', 'Cat', 'Fulton');
INSERT INTO pets (Name, Type, Family) VALUES ('Penny', 'Cat', 'Fulton');

show databases;

SELECT * FROM Pets;
