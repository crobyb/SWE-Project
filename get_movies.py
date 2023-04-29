import mysql.connector

def connect_to_db():
    try:
        # Connect to MySQL database
        conn = mysql.connector.connect(
            host="db-mysql-nyc1-30956-do-user-3263304-0.b.db.ondigitalocean.com",  # replace with your MySQL host
            user="doadmin",  # replace with your MySQL username
            password="AVNS_GHgC3IFDsdQ2Uuivp0s",  # replace with your MySQL password
            port="25060",
            auth_plugin='mysql_native_password',
            database="defaultdb"  # replace with your MySQL database name
            # sslmode='REQUIRED'
        )
        if conn.is_connected():
            print("Connected to MySQL database")
            return conn
    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL database: {e}")
        return None

def query_database(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result

# Example usage:
conn = connect_to_db()
if conn:
    # Query the database
    query = "SELECT * FROM movies"
    result = query_database(conn, query)
    if result:
        print("Results:")
        for row in result:
            print(row)
    else:
        print("No results")
    conn.close()
