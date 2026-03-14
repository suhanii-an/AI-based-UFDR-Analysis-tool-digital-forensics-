from database import connect_db

conn = connect_db()

print("Database connected successfully!")

conn.close()