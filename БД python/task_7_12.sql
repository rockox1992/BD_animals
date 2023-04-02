-- Создадим БД
DROP DATABASE IF EXISTS Animals;
CREATE DATABASE Animals;
USE Animals;

-- Создадим таблицу домашних животных
DROP TABLE IF EXISTS Pets;
CREATE TABLE Pets(
	id SERIAL PRIMARY KEY,
	cat_id BIGINT UNSIGNED NOT NULL,
	dog_id BIGINT UNSIGNED NOT NULL,
	hamster_id BIGINT UNSIGNED NOT NULL
);

-- Создадим таблицу вьючных животных
DROP TABLE IF EXISTS Pack_animals;
CREATE TABLE Pack_animals(
	id SERIAL PRIMARY KEY,
	horse_id BIGINT UNSIGNED NOT NULL,
	camel_id BIGINT UNSIGNED NOT NULL, 
	donkey_id BIGINT UNSIGNED NOT NULL
);

-- создадим таблицу котов
DROP TABLE IF EXISTS cat;
CREATE TABLE cat(
	id SERIAL PRIMARY KEY,
	name VARCHAR(40),
	Command VARCHAR(45),
    Birthday DATE
);

-- создадим таблицу собак
DROP TABLE IF EXISTS dog;
CREATE TABLE dog(
	id SERIAL PRIMARY KEY,
	name VARCHAR(40),
	Command VARCHAR(45),
    Birthday DATE
   );

  -- создадим таблицу хомяков
DROP TABLE IF EXISTS hamster;
CREATE TABLE hamster(
	id SERIAL PRIMARY KEY,
	name VARCHAR(40),
	Command VARCHAR(45),
    Birthday DATE	
);

-- создадим таблицу коней
DROP TABLE IF EXISTS horse;
CREATE TABLE horse(
	id SERIAL PRIMARY KEY,
	name VARCHAR(40),
	Command VARCHAR(45),
    Birthday DATE
);

-- создадим таблицу верблюдов
DROP TABLE IF EXISTS camel;
CREATE TABLE camel(
	id SERIAL PRIMARY KEY,
	name VARCHAR(40),
	Command VARCHAR(45),
    Birthday DATE	
);

-- создадим таблицу ослов
DROP TABLE IF EXISTS donkey;
CREATE TABLE donkey(
	id SERIAL PRIMARY KEY,
	name VARCHAR(40),
	Command VARCHAR(45),
    Birthday DATE
);

-- Создадим связи между таблицами
ALTER TABLE Pets ADD
FOREIGN KEY (cat_id) REFERENCES cat(id) ON UPDATE CASCADE ON DELETE CASCADE;

ALTER TABLE Pets ADD
FOREIGN KEY (dog_id) REFERENCES dog(id) ON UPDATE CASCADE ON DELETE CASCADE;

ALTER TABLE Pets ADD
FOREIGN KEY (hamster_id) REFERENCES hamster(id) ON UPDATE CASCADE ON DELETE CASCADE;

ALTER TABLE Pack_animals ADD
FOREIGN KEY (horse_id) REFERENCES horse(id) ON UPDATE CASCADE ON DELETE CASCADE;

ALTER TABLE Pack_animals ADD
FOREIGN KEY (camel_id) REFERENCES camel(id) ON UPDATE CASCADE ON DELETE CASCADE;

ALTER TABLE Pack_animals ADD
FOREIGN KEY (donkey_id) REFERENCES donkey(id) ON UPDATE CASCADE ON DELETE CASCADE;

-- Заполним таблицы
INSERT INTO cat (name, Command, Birthday) VALUES
('Барсик', 'Спать', '2021-05-09'),
('Мурзик', 'Пшел вон', '2022-06-09'),
('Юсуп', 'Охота', '1997-09-09')

INSERT INTO dog (name, Command, Birthday) VALUES
('Полкан', 'апорт', '1999-07-09'),
('Офицер', 'голос', '2023-08-09'),
('Муха', 'ждать', '2022-11-09')

INSERT INTO hamster  (name, Command, Birthday) VALUES
('Чип', 'Ко мне', '1999-12-09'),
('Дип', 'Лежать', '1928-01-09'),
('Дейл', 'По норам', '2021-02-09')

INSERT INTO horse (name, Command, Birthday) VALUES
('Пегас', 'Стоять', '1999-03-09'),
('Таз', 'Но', '1928-04-09'),
('Уаз', 'Прррр', '1997-01-09')

INSERT INTO camel (name, Command, Birthday) VALUES
('Горб', 'Сесть', '1999-07-09'),
('Бугор', 'Встать', '1928-05-09'),
('Толя', 'Плевать', '1997-10-09')

INSERT INTO donkey (name, Command, Birthday) VALUES
('Боб', 'Стоять', '1999-08-13'),
('Трамп', 'Крутить', '2021-02-13'),
('Меркель', 'Вертеть', '1997-01-13')


-- Добавление комманд для Horse(и не только)
-- UPDATE horse
-- SET Command = concat (Command,' ', 'DFd')
-- WHERE name = 'Таз'

-- Выведем таблицы на просмотр
SELECT*FROM cat c;
SELECT*FROM dog d;
SELECT*FROM hamster h;
SELECT*FROM horse h;
SELECT*FROM camel c;
SELECT*FROM donkey d;

-- Удалим верблюдов
SET FOREIGN_KEY_CHECKS=0; -- Отключает ограничение в БД по внешнему ключу.
DROP TABLE camel;
SET FOREIGN_KEY_CHECKS=1; -- Возвращает ограничение в БД по внешнему ключу.

-- Объединяем лошадь и осла
SELECT name, Command, Birthday  FROM horse h
UNION
SELECT name, Command, Birthday FROM donkey d;

-- Создание таблицы "молодые животные" от года до 3 лет не включительно + подсчет до месяца возраст животных
DROP TABLE IF EXISTS young_animals;
CREATE TABLE young_animals(
	id SERIAL PRIMARY KEY,
	name VARCHAR(40),
	Command VARCHAR(45),
    Birthday DATE,
    age_m VARCHAR(20)
);

INSERT INTO young_animals (name, Command, Birthday, age_m)
SELECT name, Command, Birthday, TIMESTAMPDIFF(MONTH, Birthday, now()) FROM cat  h WHERE Birthday BETWEEN  now() - INTERVAL 3 YEAR + INTERVAL 1 DAY  
AND now() - INTERVAL 1 YEAR
UNION
SELECT name, Command, Birthday, TIMESTAMPDIFF(MONTH, Birthday, now()) FROM dog d WHERE Birthday BETWEEN  now() - INTERVAL 3 YEAR + INTERVAL 1 DAY  
AND now() - INTERVAL 1 YEAR
UNION
SELECT name, Command, Birthday, TIMESTAMPDIFF(MONTH, Birthday, now()) FROM hamster  WHERE Birthday BETWEEN  now() - INTERVAL 3 YEAR + INTERVAL 1 DAY  
AND now() - INTERVAL 1 YEAR
UNION
SELECT name, Command, Birthday, TIMESTAMPDIFF(MONTH, Birthday, now()) FROM horse  WHERE Birthday BETWEEN  now() - INTERVAL 3 YEAR + INTERVAL 1 DAY  
AND now() - INTERVAL 1 YEAR
UNION
SELECT name, Command, Birthday, TIMESTAMPDIFF(MONTH, Birthday, now()) FROM donkey WHERE Birthday BETWEEN  now() - INTERVAL 3 YEAR + INTERVAL 1 DAY  
AND now() - INTERVAL 1 YEAR
;

SELECT * FROM young_animals;

-- Объеденим все таблицы в одну c добавлением метки таблицы
SELECT name, Command, Birthday, 'cat'  FROM cat c 
UNION
SELECT name, Command, Birthday, 'dog' FROM dog d
UNION
SELECT name, Command, Birthday, 'hamster' FROM hamster h 
UNION
SELECT name, Command, Birthday, 'horse' FROM horse
UNION
SELECT name, Command, Birthday, 'donkey' FROM donkey;
