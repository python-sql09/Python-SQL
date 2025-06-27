# Project Name: ETL Transformation with Script Project
# Author      : Deepa Ponnusamy
# Email       : kpdeepa1980@gmail.com,
# GitHub      : https://github.com/python-sql09/Python-SQL/tree/main/myprojects/ETL-scripting
# Date        : March 27, 2025 to May 3, 2025
# Description : Load datas to Database
# ----------------------------------------------------------------------------------------------------
import pymysql

def setup_database():
    host = 'localhost'
    user = 'root'
    password = 'Deepa@369'
    db_name = 'deeparecordshop1'

    connection = pymysql.connect(
        host=host,
        user=user,
        password=password,
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        with connection.cursor() as cursor:
            cursor.execute(f"DROP DATABASE IF EXISTS {db_name};")
            cursor.execute(f"CREATE DATABASE {db_name};")
            cursor.execute(f"USE {db_name};")

            # Create tables
            cursor.execute("""
            CREATE TABLE album (
                albumId INT AUTO_INCREMENT,
                albumTitle VARCHAR(100) NOT NULL,
                label VARCHAR(50),
                releaseDate DATE,
                price DECIMAL(5,2),
                PRIMARY KEY (albumId)
            );
            """)

            cursor.execute("""
            CREATE TABLE artist (
                artistId INT AUTO_INCREMENT,
                fname VARCHAR(25) NOT NULL,
                lname VARCHAR(50) NOT NULL,
                isHallOfFame TINYINT NOT NULL,
                PRIMARY KEY (artistId)
            );
            """)

            cursor.execute("""
            CREATE TABLE band (
                bandId INT AUTO_INCREMENT,
                bandName VARCHAR(50) NOT NULL,
                PRIMARY KEY (bandId)
            );
            """)

            cursor.execute("""
            CREATE TABLE song (
                songId INT AUTO_INCREMENT,
                songTitle VARCHAR(100) NOT NULL,
                videoUrl VARCHAR(100),
                bandId INT NOT NULL,
                PRIMARY KEY (songId),
                FOREIGN KEY (bandId) REFERENCES band(bandId)
            );
            """)

            cursor.execute("""
            CREATE TABLE songAlbum (
                songId INT,
                albumId INT,
                PRIMARY KEY (songId, albumId),
                FOREIGN KEY (songId) REFERENCES song(songId),
                FOREIGN KEY (albumId) REFERENCES album(albumId)
            );
            """)

            cursor.execute("""
            CREATE TABLE bandArtist (
                bandId INT,
                artistId INT,
                PRIMARY KEY (bandId, artistId),
                FOREIGN KEY (bandId) REFERENCES band(bandId),
                FOREIGN KEY (artistId) REFERENCES artist(artistId)
            );
            """)

            # Insert data into album table
            cursor.execute("""
            INSERT INTO album (albumId, albumTitle, releaseDate, price, label) VALUES
            (1, 'Imagine', '1971-09-09', 9.99, 'Apple'),
            (2, '22525 (Exordium & Terminus)', '1969-07-01', 25.99, 'RCA'),
            (3, "No One's Gonna Change Our World", '1969-12-12', 39.35, 'Regal Starline'),
            (4, 'Moondance Studio Album', '1969-08-01', 14.99, 'Warner Bros'),
            (5, 'Clouds', '1969-05-01', 9.99, 'Reprise'),
            (6, 'Sounds of Silence Studio Album', '1966-01-17', 9.99, 'Columbia'),
            (7,'Abbey Road', '1969-01-10', 12.99, 'Apple'),
            (9, 'Smiley Smile', '1967-09-18', 5.99, 'Capitol');
            """)

            # Insert data into artist table
            cursor.execute("""
            INSERT INTO artist (artistId, fname, lname, isHallOfFame) VALUES  
            (1, 'John', 'Lennon', 1),
            (2, 'Paul', 'McCartney', 1),
            (3, 'George', 'Harrison', 1),
            (4, 'Ringo', 'Starr', 1),
            (5, 'Denny', 'Zager', 0),
            (6, 'Rick', 'Evans', 0),
            (10, 'Van', 'Morrison', 1),
            (11, 'Judy', 'Collins', 0),
            (12, 'Paul', 'Simon', 1),
            (13, 'Art', 'Garfunkel', 0),
            (14, 'Brian', 'Wilson', 0),
            (15, 'Dennis', 'Wilson', 0),
            (16, 'Carl', 'Wilson', 0),
            (17, 'Ricky', 'Fataar', 0),
            (18, 'Blondie', 'Chaplin', 0),
            (19, 'Jimmy', 'Page', 0),
            (20, 'Robert', 'Plant', 0),
            (21, 'John Paul', 'Jones', 0),
            (22, 'John', 'Bonham', 0),
            (23, 'Mike', 'Love', 0),
            (24, 'Al', 'Jardine', 0),
            (25, 'David', 'Marks', 0),
            (26, 'Bruce', 'Johnston', 0);
            """)
            
            # Insert data into band table
            cursor.execute("""
            INSERT INTO band (bandId, bandName) VALUES 
            (1, 'The Beatles'),
            (2, 'Zager and Evans'),
            (3, 'Van Morrison'),
            (4, 'Judy Collins'),
            (5, 'Simon and Garfunkel'),
            (7, 'Beach Boys'),
            (8, 'Led Zeppelin');
            """)

            # Insert data into song table
            cursor.execute("""
            INSERT INTO song (songId, songTitle, videoUrl, bandId) VALUES 
            (1, 'Imagine', 'https://youtu.be/DVg2EJvvlF8', 1),
            (2, 'In the Year 2525', 'https://youtu.be/izQB2-Kmiic', 2),
            (3, 'Across the Universe', 'https://youtu.be/Tjq9LmSO1eI', 1),
            (4, 'Moondance', 'https://youtu.be/6lFxGBB4UG', 3),
            (5, 'Both Sides Now', 'https://youtu.be/rQOuxByR5VI', 4),
            (6, 'Sounds of Silence', 'https://youtu.be/qn0QBXMYXsM', 5),
            (7, 'Something', 'https://youtu.be/xLGe-QzCK4Q', 1),
            (9, 'Good Vibrations', 'https://youtu.be/d8rd53WuojE', 7),
            (10, 'Come Together', 'https://youtu.be/_HONxwhwmgU', 1),
            (11, 'Something', 'https://youtu.be/UKAp-jRUp2o', 1),
            (12, "Maxwell's Silver Hammer", 'https://youtu.be/YQgsob_o1io', 1);
            """)

            # Insert data into songAlbum table
            cursor.execute("""
            INSERT INTO songAlbum (songId, albumId) VALUES  
            (1,1), (2,2), (3,3), (4,4), (5,5), (6,6),
            (7,7), (9,9), (10,7), (11,7), (12,7);
            """)

            

            # Insert data into bandArtist table
            cursor.execute("""
            INSERT INTO bandArtist (bandId, artistId) VALUES  
            (1,1), (1,2), (1,3), (1,4), (2,5), (2,6),
            (3,10), (4,11), (5,12), (5,13), (7,14), (7,15),
            (7,16), (7,17), (7,18), (8,19), (8,20), (8,21),
            (8,22), (7,23), (7,24), (7,25), (7,26);
            """)

            connection.commit()

            print("Database, tables, and data inserted successfully!")

    finally:
        connection.close()

# Execute the function
setup_database()