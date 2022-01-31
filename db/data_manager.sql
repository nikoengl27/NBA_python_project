DROP TABLE IF EXISTS players;
DROP TABLE IF EXISTS teams;

CREATE TABLE teams (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    stadium VARCHAR(255),
    wins INT,
    losses INT
);

CREATE TABLE players (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    position VARCHAR(255),
    team_id INT REFERENCES teams(id) ON DELETE CASCADE
);
