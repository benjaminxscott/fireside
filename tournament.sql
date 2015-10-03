-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


create table players (
    player_id serial primary key,
    name text NOT NULL,
    wins int CHECK (wins >= 0),
    matches_played int CHECK (matches_played >= 0)
);

create table matches (
    match_id serial primary key,
    winner_id int NOT NULL,
    loser_id int NOT NULL
);
