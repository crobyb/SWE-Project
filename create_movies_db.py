import mysql.connector

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

# Create the "moviestwo" table
c.execute('''
    CREATE TABLE IF NOT EXISTS moviestwo (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        date DATE NOT NULL,
        time TIME NOT NULL,
        description TEXT NOT NULL,
        theater VARCHAR(255) NOT NULL,
        location VARCHAR(255) NOT NULL
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Table 'moviestwo' created successfully!")
