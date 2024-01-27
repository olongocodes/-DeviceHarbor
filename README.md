# -DeviceHarbor

Overview

    This is a Flask-based backend system for a simple e-commerce application. The system includes functionality for user registration, authentication, product management, and order processing. It utilizes Flask extensions such as Flask-Migrate for database migrations, Flask-RESTful for building RESTful APIs, Flask-JWT-Extended for JSON Web Token (JWT) based authentication, and Flask-CORS for handling Cross-Origin Resource Sharing.

Getting Started
    Clone the Repository:

bash
    Copy code
    git clone <repository-url>
    cd <repository-directory>
    Install Dependencies:

bash
    Copy code
    pip install -r requirements.txt
    Database Initialization:

bash
pipenv install 
    flask 
    flask_migrate
    flask_restful 
    flask_jwt_extended 
    flask_cors 

bash
    Run the Application:
        export FLASK_APP=main.py
        flask db init
        flask db migrate
        flask db revision --autogenerate -m "Create models"
        flask db upgrade

    Run the Application: flas run --reload / flask run / python3 main.py

bash
    Copy code
    python3 app.py
    The application will be accessible at http://127.0.0.1:5000/.

Configuration
Database Configuration:

    The SQLite database is used for simplicity. You can change the SQLALCHEMY_DATABASE_URI in app.py to use a different database.
    JWT Configuration:

    JWT secret key and token settings are configured in the app.py file.
    CORS Configuration:

    Cross-Origin Resource Sharing is configured using Flask-CORS in the app.py file.
    API Endpoints

User Registration:
    POST /register: Register a new user.

User Login:
    POST /login: Authenticate and obtain JWT tokens.

Refresh Access Token:
    POST /refresh: Refresh the access token.

User Profile:
    GET /user: Retrieve user profile information.

Product Management:
    GET /products: Get a list of all products.
    GET /products/<int:product_id>: Get details of a specific product.
    POST /products: Add a new product (Admin only).
    PUT /products/<int:product_id>: Update a product (Admin only).
    DELETE /products/<int:product_id>: Delete a product (Admin only).

Product Orders:
    POST /order: Place an order for a product.
    GET /productorders/<int:order_id>: Get details of a specific order.
    GET /productorders: Get a list of all orders (Admin only).
    PUT /productorders/<int:order_id>: Update an order (Admin only).
    DELETE /productorders/<int:order_id>: Delete an order (Admin only).

User Orders:
    GET /userorders: Get a list of user's orders.
    GET /userorders/<int:order_id>: Get details of a specific user order.

Authentication
    The system uses JWT for authentication. To access protected endpoints, include the JWT token in the request headers or cookies.

Security Considerations
    Always use HTTPS in a production environment to secure communication between clients and the server.
    Validate and sanitize user inputs to prevent security vulnerabilities.

Contributors
    1. Kevin Olongo
    2. Naomi Inyele
    3. Mikail Hassan 
    4. Emmanuel Kipngeno
