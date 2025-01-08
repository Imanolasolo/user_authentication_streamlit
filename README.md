# Generic Login and authentication with Streamlit

This project is a **Generic Login and authentication System** built with **Streamlit**, implementing authentication and role-based access control (RBAC) using JWT (JSON Web Tokens). It allows administrators to manage users and roles, while providing role-specific access to different features.

## Features

### Authentication and Authorization

- **Login System**:
  - Users can log in with a username and password.
  - Authentication is handled securely using hashed passwords.
- **JWT-based Authentication**:
  - Tokens are generated upon successful login and stored in `st.session_state`.
  - Tokens are validated to authorize access to specific pages.
- **Role-Based Access Control**:
  - Admins can create and manage users and roles.
  - Only users with the `admin` role can access the Admin Dashboard.

### Admin Dashboard

- **User Management**:
  - Add new users with specific roles.
  - View a list of all registered users.
  - Delete users.
- **Role Management**:
  - Add new roles.
  - View a list of all roles.
  - Delete roles.

## File Structure

```
user_authentication/
|
|-- auth/
|   |-- auth_manager.py      # Handles user authentication and role management.
|   |-- hash_utils.py        # Contains password hashing utilities.
|   |-- jwt_utils.py         # Handles JWT generation and decoding.
|   |-- db_manager.py        # Handles the database.
|-- ui/
|   |-- dashboard.py         # Admin dashboard for managing users and roles.
|   |-- login.py             # User login page.
|                 
|-- README.md                # Project documentation.
```

## How It Works

### Authentication Workflow

1. **Login Page**:

   - Users enter their credentials.
   - Credentials are verified using `auth_manager.authenticate_user()`.
   - A JWT is generated and stored in `st.session_state` upon successful login.

2. **Session Persistence**:

   - The token in `st.session_state` ensures session persistence across interactions.
   - Role-specific redirection is managed based on the decoded token data.

3. **Logout**:

   - Users can log out, which removes the token from `st.session_state`.

### Admin Dashboard Workflow

- **Add Users**:

  - Admins provide a username, password, and role to create a new user.
  - Passwords are hashed before storage.

- **Manage Users and Roles**:

  - Lists of users and roles are fetched from the database.
  - Admins can delete users or roles directly from the interface.

## Getting Started

### Prerequisites

- Python 3.8 or higher.
- Streamlit.
- SQLite database.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-repo/hospital-management-system.git
   cd hospital-management-system
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Initialize the database:

   ```bash
   python db_manager.py
   ```

4. Run the application:

   ```bash
   streamlit run app.py
   ```

### Default Admin Credentials

- **Username**: `admin`
- **Password**: `admin123`

## Future Improvements

- Implement support for additional roles.
- Add functionality for project modules such as admissions, users management, and billing.
- Improve UI/UX for better usability.
- Integrate secure HTTPS connections.

## Contributing

Feel free to submit issues or pull requests for improvements. Contributions are always welcome!

## License

This project is licensed under the MIT License.

---

Developed by **Imanol Asolo** and the **CodeCodix** team.

