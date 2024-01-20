import sqlite3
import os

DB_ROOT =  "./src/database"
DB_VERSION = 1


def create_database():
    if os.path.exists(os.path.join(DB_ROOT, "database.db")):
        return

    conn = sqlite3.connect(os.path.join(DB_ROOT, "database.db"))
    cursor = conn.cursor()

    with open(os.path.join(DB_ROOT, "schemas/database.sql"), "r") as schema_file:
        schema = schema_file.read()

    cursor.executescript(schema)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()

