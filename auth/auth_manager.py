import sqlite3
import streamlit as st
from .hash_utils import hash_password, verify_password
from .db_manager import DataBaseManager

class AuthManager:
    def __init__(self, db_path="auth.db"):
        self.db = DataBaseManager(db_path)
        self.create_admin_user()  # Crea el usuario admin al inicializar

    def create_admin_user(self):
        """Create the admin user from secrets if it does not exist."""
        admin_username = st.secrets["admin"]["username"]
        admin_password = hash_password(st.secrets["admin"]["password"])
        admin_role = "admin"

        # Check if the admin user already exists
        admin_exists = self.db.fetchone(
            "SELECT * FROM users WHERE username = ?",
            (admin_username,)
        )

        if not admin_exists:
            self.db.execute(
                "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
                (admin_username, admin_password, admin_role)
            )
            print("Admin user created successfully.")

    def register_user(self, username: str, password: str, role: str):
        """Register a new user in the database."""
        hashed_password = hash_password(password)
        try:
            self.db.execute(
                "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
                (username, hashed_password, role)
            )
            return True
        except sqlite3.IntegrityError:
            return False

    def authenticate_user(self, username: str, password: str):
        """Authenticates the user by verifying the credentials."""
        user = self.db.fetchone(
            "SELECT username, password, role FROM users WHERE username = ?",
            (username,)
        )
        if user and verify_password(password, user[1]):
            return {"username": user[0], "role": user[2]}
        return None

    def create_role(self, role_name: str):
        """Create a new role in the database."""
        try:
            self.db.execute("INSERT INTO roles (role_name) VALUES (?)", (role_name,))
            return True
        except sqlite3.IntegrityError:
            return False
