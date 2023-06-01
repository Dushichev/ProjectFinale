USE PROJECTWORK;

CREATE TABLE cat (
	id INT PRIMARY KEY AUTO_INCREMENT,
	animal_name CHAR(30),
    commands TEXT,
    date_of_birth DATE
);

CREATE TABLE dog (
	id INT PRIMARY KEY AUTO_INCREMENT,
	animal_name CHAR(30),
    commands TEXT,
    date_of_birth DATE
);

CREATE TABLE hamster (
	id INT PRIMARY KEY AUTO_INCREMENT,
	animal_name CHAR(30),
    commands TEXT,
    date_of_birth DATE
);

CREATE TABLE horse (
	id INT PRIMARY KEY AUTO_INCREMENT,
	animal_name CHAR(30),
    commands TEXT,
    date_of_birth DATE
);

CREATE TABLE camel (
	id INT PRIMARY KEY AUTO_INCREMENT,
	animal_name CHAR(30),
    commands TEXT,
    date_of_birth DATE
);

CREATE TABLE donkey (
	id INT PRIMARY KEY AUTO_INCREMENT,
	animal_name CHAR(30),
    commands TEXT,
    date_of_birth DATE
);

INSERT INTO cat (animal_name,commands, date_of_birth) VALUES 
	("Kotik", "meow", "1999-10-01"),
	("Ploshka", "meow, sit", "21998-11-01"),
    ("Rita", "meow, sit", "2023-01-01"),
    ("Meowitik", "meow, eat", "2019-07-08"),
    ("Tosha", "voice", "2000-04-04");
   
INSERT INTO dog (animal_name,commands, date_of_birth) VALUES 
	("Bobik", "run", "2020-07-03"),
	("Tyzik", "eat", "2020-07-03"),
    ("Rex", "left hand", "2020-01-03"),
    ("Layka", "run", "2020-04-01"),
    ("Zhora", "left hand", "2022-04-03");
    
INSERT INTO hamster (animal_name,commands, date_of_birth) VALUES 
	("Duda", "eat", "2019-03-01"),
	("Domlin", "eat", "2022-09-03"),
    ("Diko", "eat", "2023-01-02"),
    ("Dadamin", "eat", "2023-05-04"),
    ("Dotik", "run", "2000-01-12");
    
INSERT INTO horse (animal_name,commands, date_of_birth) VALUES 
	("Laska", "run", "2021-01-01"),
	("Luna", "run", "2019-12-10"),
    ("Lida", "run", "2020-02-02"),
    ("Lorik", "run", "2022-03-03"),
    ("Lana", "eat", "2018-05-05");
    
INSERT INTO camel (animal_name,commands, date_of_birth) VALUES 
	("Cama", "eat", "2022-02-02"),
	("Cuci", "eat", "2022-02-02"),
    ("Cawan", "run", "2019-12-02"),
    ("Cart", "run", "2021-01-13"),
    ("Calib", "voice", "2017-07-01");
    
INSERT INTO donkey (animal_name,commands, date_of_birth) VALUES 
	("Dudu", "eat", "2021-01-01"),
	("Dino", "eat", "2019-12-10"),
    ("Dodi", "left hand", "2020-02-02"),
    ("Dante", "right hand", "2022-03-03"),
    ("Dunik", "meow", "2018-05-05");
    
TRUNCATE camel;

INSERT INTO horse (animal_name, commands, date_of_birth)
SELECT animal_name, commands, date_of_birth
FROM donkey;

DROP TABLE donkey;

REanimal_name TABLE horse TO horse_donkey;

CREATE TABLE young_animal (
	id INT PRIMARY KEY AUTO_INCREMENT,
	animal_name CHAR(30),
    commands TEXT,
    date_of_birth DATE,
    age TEXT
);


DELIMITER $$
CREATE FUNCTION age_animal (date_b DATE)
RETURNS TEXT
DETERMINISTIC
BEGIN
    DECLARE res TEXT DEFAULT "";
	SET res = CONCAT(
            TIMESTAMPDIFF(YEAR, date_b, CURDATE()),
            " years ",
            TIMESTAMPDIFF(MONTH, date_b, CURDATE()) % 12,
            " month"
        );
	RETURN res;
END $$
DELIMITER ;

INSERT INTO young_animal (animal_name, commands, date_of_birth, age)
SELECT animal_name, commands, date_of_birth, age_animal(date_of_birth)
FROM cat
WHERE TIMESTAMPDIFF(YEAR, date_of_birth, CURDATE()) BETWEEN 1 AND 3
UNION ALL
SELECT animal_name, commands, date_of_birth, age_animal(date_of_birth)
FROM dog
WHERE TIMESTAMPDIFF(YEAR, date_of_birth, CURDATE()) BETWEEN 1 AND 3
UNION ALL
SELECT animal_name, commands, date_of_birth, age_animal(date_of_birth)
FROM hamster
WHERE TIMESTAMPDIFF(YEAR, date_of_birth, CURDATE()) BETWEEN 1 AND 3
UNION ALL
SELECT animal_name, commands, date_of_birth, age_animal(date_of_birth)
FROM horse_donkey
WHERE TIMESTAMPDIFF(YEAR, date_of_birth, CURDATE()) BETWEEN 1 AND 3;

SET SQL_SAFE_UPDATES = 0;

DELETE FROM cat 
WHERE TIMESTAMPDIFF(YEAR, cat.date_of_birth, CURDATE()) IN (1, 2, 3);

DELETE FROM dog 
WHERE TIMESTAMPDIFF(YEAR, date_of_birth, CURDATE()) BETWEEN 1 AND 3;

DELETE FROM hamster 
WHERE TIMESTAMPDIFF(YEAR, date_of_birth, CURDATE()) BETWEEN 1 AND 3;

DELETE FROM horse_donkey 
WHERE TIMESTAMPDIFF(YEAR, date_of_birth, CURDATE()) BETWEEN 1 AND 3;

CREATE TABLE animals (
	id INT PRIMARY KEY AUTO_INCREMENT,
	animal_name CHAR(30),
    commands TEXT,
    date_of_birth DATE,
    age TEXT,
    animal_type ENUM("cat","dog","hamster", "horse_donkey", "young_animals") NOT NULL
);

INSERT INTO animals (animal_name, commands, date_of_birth, age, animal_type)
SELECT animal_name, commands, date_of_birth, age_animal(date_of_birth), "cat"
FROM cat;

INSERT INTO animals (animal_name, commands, date_of_birth, age, animal_type)
SELECT animal_name, commands, date_of_birth, age_animal(date_of_birth), "dog"
FROM dog;

INSERT INTO animals (animal_name, commands, date_of_birth, age, animal_type)
SELECT animal_name, commands, date_of_birth, age_animal(date_of_birth), "hamster"
FROM hamster;

INSERT INTO animals (animal_name, commands, date_of_birth, age, animal_type)
SELECT animal_name, commands, date_of_birth, age_animal(date_of_birth), "horse_donkey"
FROM horse_donkey;

INSERT INTO animals (animal_name, commands, date_of_birth, age, animal_type)
SELECT animal_name, commands, date_of_birth, age_animal(date_of_birth), "young_animals"
FROM young_animal;