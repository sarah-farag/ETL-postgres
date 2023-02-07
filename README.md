# Introduction
***
A startup compnay 'Sparkify ', has been collecting data regarding songs and log activity for their users, they want to analyze this data to find what are the users listening to.

The data is saved in a directory in the format JSON for both the user activity log and the meta data on their songs, this is hard to queny on or analyze, 

# How To Run
***
To get set/generate the tables in your database, run :

    python create_tables.py

After that, to run the ETL-pipeline script run :

    python etl.py

# Database schema
***
Here is the database schema in a star schema format , with one fact table *songplays* and the four dimension tables *songs*,*users*,*artist* , and *time*

![Alt text](/assets/star schema.png "Database schema")

# ETL
***
>This has two functions : 
>1. process_song_file
> where the data is extracted from the song data file, transfered and then added to the respective  tables 
>
>
>2. process_log_file
> where the data is extracted from the log data file, transfered and then added to the respective  tables 