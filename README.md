# Create a new database and table and insert demo data
    CREATE DATABASE RESTAPIDEMO;

    create table person (
        id serial primary key,
        name varchar(100),
        age int,
        student boolean
    );


    insert into person (name, age, student) values ('Alice', 20, true);

# Crete database.ini file to src/data/database.ini path.
    [postgresql]
    host=
    database=
    port=
    user=
    password=

# Open command prompt in VSCode editor

## Create python virtual environment
    python -m venv venv
    .\venv\Scripts\activate

## Install libraries
    pip install -r requirements.txt

## Start server
    python src\data\person_api.py

