Flask User Management REST API
**Introduction**
This project is a simple, foundational RESTful API for managing user data. Built with Python and the Flask framework, it demonstrates the core principles of API development by providing endpoints for essential CRUD (Create, Read, Update, Delete) operations. The user data is stored in an in-memory dictionary, making it a perfect lightweight project for learning and understanding API design without the complexity of a database.
**Features**
Create Users: Add new user data with a POST request.

Read Users: Retrieve a list of all users or a single user by their unique ID with GET requests.

Update Users: Modify an existing user's details with a PUT request.

Delete Users: Remove a user from the system with a DELETE request.

JSON Support: All API interactions use JSON for data exchange.

Error Handling: The API returns appropriate HTTP status codes and error messages for invalid requests or non-existent resources (e.g., 404 Not Found).

**Technologies Used**
Python 3: The programming language for the backend logic.

Flask: A lightweight and flexible web framework for building the API.

pip: The Python package installer.

Postman / cURL: Recommended tools for testing the API endpoints.

**Setup and Installation**
Follow these steps to set up and run the project locally.