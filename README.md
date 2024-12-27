# ChatSystemAPI

ChatApi is now live and accessible to everyone. For now, data is stored temporarily using an SQLite3 database, and AI responses might be delayed occasionally because OpenAI requires premium access for uninterrupted performance. Rest assured, both the database and response times will be improved with upcoming updates.


https://chatapi-1e6w.onrender.com/api/login


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

![1000625637](https://github.com/user-attachments/assets/1a800b2c-a4e5-464e-876c-617434f699ef)




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

    "password": "securepassword***"
}

Response JSON (Success):

{

    "token": "abcd1234efgh5678ijkl"
}

Response JSON (Error):

{

    "error": "Invalid credentials"
}


![1000625638](https://github.com/user-attachments/assets/6730a143-622c-49f9-aad1-e353cb2ab406)

![1000625640](https://github.com/user-attachments/assets/84624732-8fa6-499f-9272-53fcb407a3ac)


![1000625639](https://github.com/user-attachments/assets/40561bc5-b0fd-4fc8-bb85-3a9e8b8b96af)


Task 3: Chat API

How It Works:

1. The user sends a POST request to the /api/chat/ endpoint with their message and token.


2. The server:

Authenticates the user using the token.

Deducts 100 tokens from the user's balance on every chat request.

Generates an AI response for the provided message.

Saves the chat (user, message, AI response, and timestamp) to the database.

Returns the AI response to the user.


3. If authentication fails, insufficient tokens, or other errors, appropriate error messages are returned.



API Request Structure:

Endpoint: /api/chat/

HTTP Method: POST

Request JSON:

{

    "token" : "ahdudjdis****"
    "message": "Hello, how are you?"
}

Response JSON (Success):

{

    "message": "Hello, how are you?",
    "response": "AI response to 'Hello, how are you?'"
}

Response JSON (Error: Insufficient Tokens):

{

    "error": "Insufficient tokens"
}

Response JSON (Error: Unauthorized):

{

    "detail": "Authentication credentials were not provided."
}


![1000628943](https://github.com/user-attachments/assets/98d5664f-fd40-4b24-a642-992080f553bd)


Task 4: Token Balance API

How It Works:

1. The user sends a POST request to the /api/balance/ endpoint


2. The server:

Authenticates the user using the token.

Fetches the current token_balance for the user.

Returns the balance in the response.



3. If authentication fails, an appropriate error message is returned.



API Request Structure:

Endpoint:
/api/balance/

HTTP Method:
POST

Response JSON (Success):

{

    "token_balance": 3800
}


![1000625643](https://github.com/user-attachments/assets/a51aecf3-f4d4-42c0-868a-624eb4dfe087)


Response JSON (Error: Unmatched token):

{

     "error": "An unexpected error occurred: Token matching query does not exist."
}

![1000630131](https://github.com/user-attachments/assets/1a222440-a849-4067-8d17-c33fd57a8f51)


Response JSON (Error: login is required):

{

         "error": "login before checking balance"
}

![1000630130](https://github.com/user-attachments/assets/fdc0b279-b4a1-47be-8869-b9a67e3c9a69)


These API structures provide a comprehensive flow for managing user registration, authentication, chat functionality, and token tracking.

