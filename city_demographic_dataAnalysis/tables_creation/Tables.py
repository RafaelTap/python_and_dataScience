import psycopg2 as connector


connection = connector.connect("city.db")
cursor = connection.cursor()

command = """ 
            CREATE TABLE person IF NOT EXISTS (
               personId INT NOT NULL AUTO INCREMENT,
               name VARCHAR(60) NOT NULL,
               age INT NOT NULL,
               gender VAR NOT NULL,
               document VARCHAR(11) NOT NULL,
               PRIMARY KEY personId
               );
            CREATE TABLE address IF NOT EXISTS (
                addressId INT NOT NULL AUTO INCREMENT,
                street VARCHAR NOT NULL,
                number INT NOT NULL,
                complement VARCHAR(20),
                postCode VARCHAR(9),
                personId INT NOT NULL,
                PRIMARY KEY addressId,
                CONSTRAINT FOREIGN KEY personId REFERENCES person (personId)
               );
            CREATE TABLE discipline IF NOT EXISTS (
                disciplineId INT NOT NULL AUTO INCREMENT,
                name VARCHAR (45) NOT NULL,
                PRIMARY KEY disciplineId
               );
            CREATE TABLE person_discipline (
                personId INT,
                discipline INT,
                CONSTRAINT FOREIGN KEY personId REFERENCES person (personId),
                CONSTRAINT FOREIGN KEY disciplineId REFERENCES discipline (disciplineId)
               );
               """

cursor.execute(command)
connection.commit()

cursor.close()
connection.close()