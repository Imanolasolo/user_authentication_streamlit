import sqlite3
import os

class DataBaseManager:
    def __init__(self, db_name="database.db"):
        """
        Initializes the database manager.
       Create the database if it does not exist.
        """
        self.db_name = db_name
        self.connection = None
        self.create_tables()

    def connect(self):
        """Connect to the database."""
        self.connection = sqlite3.connect(self.db_name)
        return self.connection

    def execute(self, query, params=()):
        """Executes a SQL query."""
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
        return cursor

    def fetchall(self, query, params=()):
        """Executes a SELECT query and returns all the results."""
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute(query, params)
        return cursor.fetchall()
    
    def fetchone(self, query, params=()):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute(query, params)
        return cursor.fetchone()

    def create_tables(self):
        """Create the necessary tables in the database."""
        users_table = """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL
        );
        """
        roles_table = """
        CREATE TABLE IF NOT EXISTS roles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            role_name TEXT UNIQUE NOT NULL
        );
        """
        self.execute(users_table)
        self.execute(roles_table)

# Initialize the database by running this script
if __name__ == "__main__":
    db_manager = DataBaseManager("database.db")
    print(f"Database '{db_manager.db_name}' correctly initialized.")
