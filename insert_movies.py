import mysql.connector
import json

# Connect to the MySQL database
conn = mysql.connector.connect(
    host="db-mysql-nyc1-30956-do-user-3263304-0.b.db.ondigitalocean.com",  # replace with your MySQL host
    user="doadmin",  # replace with your MySQL username
    password="AVNS_GHgC3IFDsdQ2Uuivp0s",  # replace with your MySQL password
    port="25060",
    auth_plugin='mysql_native_password',
    database="defaultdb"  # replace with your MySQL database name
)

# Create a cursor to interact with the database
c = conn.cursor()

# Load data from JSON file
with open("movies.json", "r") as file:
    data = json.load(file)

# Loop through each movie and insert into the database
for movie in data:
    title = movie["title"]
    date = movie["date"]
    time = movie["time"]
    description = movie["description"]
    theater = movie["theater"]
    location = movie["location"]

    # Insert movie data into the "moviestwo" table
    c.execute('''
        INSERT INTO moviestwo (title, date, time, description, theater, location)
        VALUES (%s, %s, %s, %s, %s, %s)
    ''', (title, date, time, description, theater, location))

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Data inserted into 'moviestwo' table successfully!")
