import psycopg2

def connect_to_postgresql():
    try:
        # Connect to your PostgreSQL database by providing the necessary connection details
        conn = psycopg2.connect(
            dbname="msf",
            user="postgres",
            password="qwer4099",
            host="192.168.91.128",
            port="5432"
        )
        
        # Create a cursor object to execute SQL queries
        cursor = conn.cursor()
        
        # Example: Execute a SQL query
        cursor.execute("SELECT version();")
        
        # Fetch the result
        db_version = cursor.fetchone()
        print("PostgreSQL database version:", db_version)
        
        # Don't forget to close the cursor and connection
        cursor.close()
        conn.close()
        
    except psycopg2.Error as e:
        print("Error connecting to PostgreSQL:", e)

if __name__ == "__main__":
    connect_to_postgresql()
