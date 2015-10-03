#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database cursor."""

    dbname = "fireside"
    dbconnection = psycopg2.connect("dbname=fireside")    
    dbconnection.autocommit = True
    
    return dbconnection.cursor()
    # PERF need to teardown the connection / cursors as well to avoid exhaustion     


def deleteMatches():
    """Remove all the match records from the database."""
    dbcursor = connect()
    dbcursor.execute("TRUNCATE matches")
    
    return 1 # success

def deletePlayers():
    """Remove all the player records from the database."""
    dbcursor = connect()
    dbcursor.execute("TRUNCATE players")
    
    return 1 # success


def countPlayers():
    """Returns the number of players currently registered."""
    
    dbcursor = connect()
    dbcursor.execute("SELECT * from players")
    return dbcursor.rowcount


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """

    dbcursor = connect()
    dbcursor.execute("INSERT INTO players (name, wins, matches_played) VALUES (%s, %s, %s)",
        (name, 0, 0 ))

    return 1 # success

def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    
    dbcursor = connect()
    dbcursor.execute("SELECT * from players;")
    
    # TODO rankings = 


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
 
    dbcursor = connect()
 
    # insert match 
    dbcursor.execute("INSERT INTO matches (winner_id, loser_id) VALUES (%s, %s)",
        (winner, loser))
    
    # PERF wins and total matches are tracked in player DB, trading off disk and a slightly more complex insert for a constant time lookup
    
    # increment win in player table
    dbcursor.execute("update players set wins = wins + 1 where player_id = (%s)",
        (winner,))
    
    # increment matches for both players
    dbcursor.execute("update players set matches_played = matches_played + 1 where player_id = %s",
        (winner,))
    dbcursor.execute("update players set matches_played = matches_played + 1 where player_id = %s",
        (loser,))
        
    # PERF could merge these updates to save a db query
    
 
    return 1 #success
 
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """


