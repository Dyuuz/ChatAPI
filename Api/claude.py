import requests

# Replace this with your Claude API key
API_KEY = 'your_Claude_API_key'

# Claude API endpoint (replace with the correct endpoint if different)
API_URL = 'https://api.anthropic.com/v1/claude/completions'

# Function to send user input and get AI response
def get_ai_response(user_input):
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }

    # Prepare the payload (input text to send to Claude)
    payload = {
        'model': 'claude-v1',  # Specify the Claude model (use the latest version available)
        'prompt': user_input,  # User's input text
        'max_tokens': 150,     # Set the maximum number of tokens for the response
        'temperature': 0.7,    # Control the randomness of the response (0.0 to 1.0)
    }

    # Make the API request
    response = requests.post(API_URL, json=payload, headers=headers)

    if response.status_code == 200:
        # Get the AI-generated response from Claude
        response_data = response.json()
        return response_data['choices'][0]['text'].strip()
    else:
        return f"Error: {response.status_code}, {response.text}"

# Main function to interact with the user
def main():
    print("Welcome! Ask me anything:")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        ai_response = get_ai_response(user_input)
        print(f"Claude: {ai_response}")

if __name__ == "__main__":
    main()
