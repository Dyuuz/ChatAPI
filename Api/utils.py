import openai

# Set your OpenAI API key
openai.api_key = "settings.API_KEY"

# Example request to the GPT model
def get_ai_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use "gpt-4" if you have access
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
            max_tokens=100,  # Limit the response length
            temperature=0.7,  # Adjust creativity level
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error: {e}"