CREATE KEYSPACE IF NOT EXISTS my_test_app WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};

USE my_test_app;

CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password TEXT
);

INSERT INTO users (username, password) VALUES ('alice', '123456');
INSERT INTO users (username, password) VALUES ('bob', 'asdqwe');
INSERT INTO users (username, password) VALUES ('admin', 'Tona6e5rVaJ7Neyo#h^uRr8FYDDv*G!*');

