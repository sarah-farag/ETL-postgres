# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artist"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays
                        (songplay_id SERIAL PRIMARY KEY, 
                         start_time timestamp NOT NULL, user_id int NOT NULL, 
                         level text, song_id text, artist_id text,
                         session_id int, location text, user_agent text)
;""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users ( user_id  SERIAL PRIMARY KEY, first_name text , last_name text , gender text, level text
);


""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs(song_id text PRIMARY KEY, title text not null, artist_id text not null, year int ,duration double precision not null
);
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artist (artist_id text PRIMARY KEY, name text not null, location text, latitude text, longitude text
);
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time (start_time timestamp PRIMARY KEY, hour int, day int, week int,month int, year int, weekday int
);
""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays
                        (start_time, user_id, level, song_id,
                         artist_id, session_id, location, user_agent)
                         VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                         ON CONFLICT (songplay_id) DO NOTHING
;""")
user_table_insert = ("""
INSERT INTO users(user_id,first_name,last_name,gender,level)
VALUES (%s,%s,%s,%s,%s)
ON CONFLICT (user_id) DO NOTHING
""")

song_table_insert = ("""
INSERT INTO songs (song_id,title,artist_id,year,duration)
VALUES (%s,%s,%s,%s,%s)
ON CONFLICT (song_id) DO NOTHING    
""")

artist_table_insert = ("""
INSERT INTO artist (artist_id,name,location,latitude,longitude)
VALUES (%s,%s,%s,%s,%s)
ON CONFLICT (artist_id) DO NOTHING
""")


time_table_insert = ("""
INSERT INTO time(start_time, hour, day, week, month, year, weekday)
VALUES (%s, %s, %s, %s, %s, %s, %s)
ON CONFLICT (start_time) DO NOTHING
""")

# FIND SONGS
#Implement the song_select query in sql_queries.py to find the song ID and artist ID based on the title, artist name, and duration of a song.

song_select = ("""
SELECT songs.song_id ,songs.artist_id
FROM songs INNER JOIN artist
ON songs.artist_id=artist.artist_id
WHERE  songs.title = %s
       AND artist.name = %s
       AND songs.duration = %s;
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]n