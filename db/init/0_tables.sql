DROP TABLE IF EXISTS feeds;

CREATE TABLE feeds (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    url VARCHAR(255) UNIQUE NOT NULL
);