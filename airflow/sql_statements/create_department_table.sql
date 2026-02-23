CREATE TABLE IF NOT EXISTS {{params.departments_table}} (
            id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            name VARCHAR(50) NOT NULL
        )