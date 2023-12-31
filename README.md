<!-- Title -->
# Flask Login Template

<!-- Badges -->
![Made with Python](https://img.shields.io/badge/made%20with-Python-blue.svg)
![License MIT](https://img.shields.io/badge/license-MIT-green.svg)

<!-- About the Project -->
## About the Project 🚀

Flask Login Template is a simple and customizable authentication template built with Flask and Tailwind CSS. It provides a user-friendly login and signup experience with modern UI elements and features.

<!-- Features -->
## Key Features 🌟

- **User Authentication**: Secure user authentication using Flask and Werkzeug.
- **Modern UI**: Professionally designed login and signup forms with Tailwind CSS.
- **Responsive**: Works seamlessly on various screen sizes.

<!-- Getting Started -->
## Getting Started 🚦

To get started, follow these steps:

1. Clone the repository.
   ```bash
   git clone https://github.com/ichliebees/Login-Template-Flask.git
   ```

2. Run the application.
   ```bash
   python main.py
   ```

3. Open the app in your browser: [http://localhost:5000](http://localhost:5000)

<!-- Usage -->
## Usage 🚀

- Customize the templates in the `templates/` folder for your specific needs.
- Enhance the style using Tailwind CSS in the `static/style.css` file.
- Extend the functionality based on your project requirements.

<!-- Features -->
## Features ✨

- **Hashing**: Secure password hashing using the SHA-256 algorithm.
- **Session Management**: Flask session for user authentication.
- **Responsive Design**: Tailwind CSS for a modern and responsive UI.

<!-- Database Configuration -->
## Database Configuration 🛡️

This template uses a simple JSON file (`users.json`) to store user information for quick setup and testing. However, for a production environment, it's recommended to set up a secure database.

### Steps to Set Up a Database:

1. Choose a Database: Select a suitable database system (e.g., PostgreSQL, MySQL, SQLite).

2. Install Database Engine: Install the necessary database engine and libraries.

3. Update Configuration: Modify the `main.py` file to use your database configuration.

    ```python
    # Replace these lines with your database configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'your_database_uri'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    ```

4. Create User Table: Define a `User` model and create the necessary database tables.

    ```python
    from flask_sqlalchemy import SQLAlchemy

    db = SQLAlchemy(app)

    class User(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(50), unique=True, nullable=False)
        password = db.Column(db.String(100), nullable=False)
    ```

5. Migrate Database: Run migrations to apply changes to the database.

    ```bash
    flask db init
    flask db migrate
    flask db upgrade
    ```

### Secure Database Operations:

- **Use SQLAlchemy ORM**: Leverage SQLAlchemy ORM to perform secure database operations and prevent SQL injection.

- **Hashed Passwords**: Store hashed passwords using a secure hashing algorithm.

- **Input Validation**: Implement proper input validation to prevent malicious attacks.

**Note:** Always follow best practices for database security and user authentication when deploying to a production environment.

<!-- JSON File -->
## JSON File 📋

This template uses a simple JSON file (`users.json`) to store user information for quick setup and testing. While convenient for development, it's not suitable for production due to security concerns.

### Secure JSON File Operations:

- **Restrict Access**: Ensure proper file permissions to restrict access.

- **Backup Regularly**: Regularly back up the JSON file to prevent data loss.

- **Limit Sensitive Data**: Avoid storing sensitive information directly in the JSON file.

<!-- Security -->
## Security 🔐

This template follows security best practices:

- **Password Hashing**: User passwords are securely hashed using the SHA-256 algorithm.

- **Session Management**: Flask session management for secure user authentication.

- **Secure Forms**: Proper validation and sanitation of user inputs in forms.

- **HTTPS**: Deploy the application with HTTPS for secure communication.

Always stay informed about the latest security updates and adapt the template accordingly.




<!-- License -->
## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

<!-- Acknowledgments -->
## Acknowledgments 🙌

- Flask: [https://flask.palletsprojects.com/](https://flask.palletsprojects.com/)
- Tailwind CSS: [https://tailwindcss.com/](https://tailwindcss.com/)


<!-- Preview -->
## Preview 🚀

Take a glimpse of the sleek and user-friendly login template. The following screenshots showcase the login, signup, and dashboard pages, along with alerts for incorrect password and password mismatch.

### Login Page:

![Login Page](https://github.com/ichliebees/Login-Template-Flask/assets/138697155/6f38df61-b4a7-4f8f-a4bc-bc62c1d3d4a4)

### Invalid Password Alert:

![Invalid Password Alert](https://github.com/ichliebees/Login-Template-Flask/assets/138697155/1ec24d84-b5cc-4168-95f5-131209d14aeb)

### Signup Page:

![Signup Page](https://github.com/ichliebees/Login-Template-Flask/assets/138697155/72208a5f-0d53-466e-8abb-079d9dbca47f)

### Password Mismatch Alert:

![Password Mismatch Alert](https://github.com/ichliebees/Login-Template-Flask/assets/138697155/d21cb890-a052-4fa1-b697-322761ab91ad)

### Dashboard Page:

![Dashboard Page](https://github.com/ichliebees/Login-Template-Flask/assets/138697155/60f3a2a2-de7a-4ba5-bbe5-379a92d9d6fe)

---

### Explore More:

Feel free to explore the features, security measures, and customization options in this Flask login template. If you encounter any issues or have suggestions for improvements, don't hesitate to contribute or open an issue.

Your feedback is valuable! 🌟


