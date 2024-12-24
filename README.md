# ChatSystemAPI

Here’s a detailed explanation of how each task works, along with the API request structure to interact with it:

Task 1: User Registration API

How It Works:

The user sends a POST request to the /api/register/ endpoint with a JSON payload containing their username and password.
The server validates the data using the UserRegistrationSerializer.

If valid:

A new user is created.
The token_balance is initialized to 4000.
A success message is returned.

If invalid:

Error messages are returned explaining why the registration failed.

API Request Structure:

Endpoint: /api/register/

HTTP Method:
POST

Request JSON format:

{

    "username": "testuser***",

    "password": "*****"
}


![bandicam 2024-12-24 09-09-08-747](https://github.com/user-attachments/assets/3a732b34-d80a-41e6-8bc6-79fb2144150b)


Task 2: User Login API

How It Works:

1. The user sends a POST request to the /api/login/ endpoint with their username and password.


2. The server authenticates the credentials:

If valid, a token is generated (or generates new token if it already exists) for account security.

The token is returned to the user.

The user can use this token for authenticated API calls like sending chat requests.

If invalid, an error message is returned.


API Request Structure:

Endpoint: /api/login/

HTTP Method: POST

Request JSON:

{

    "username": "testuser",

    "password": "securepassword123"
}

Response JSON (Success):

{

    "token": "abcd1234efgh5678ijkl"
}

Response JSON (Error):

{

    "error": "Invalid credentials"
}


