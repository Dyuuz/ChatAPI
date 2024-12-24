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





![bandicam 2024-12-24 09-09-08-747](https://github.com/user-attachments/assets/3a732b34-d80a-41e6-8bc6-79fb2144150b)

