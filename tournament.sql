-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


create table players (
    player_id int primary key,
    name text NOT NULL,
    wins int
);

create table matches (
    match_id int primary key,
    player1_id int NOT NULL,
    player2_id int NOT NULL
);
