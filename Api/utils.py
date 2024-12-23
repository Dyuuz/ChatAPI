import time
import openai
import os
from django.conf import settings
#from openai import OpenAI
#from openai.types import Completion, CompletionChoice, CompletionUsage, ChatModel

# Set your API key
def get_ai_response(message):
    try:
        openai.api_key = os.environ.get(settings.API_KEY),  # This is the default and can be omitted
        

        chat_completion = openai.ChatCompletion.create(
            messages=[
                {
                    "role": "user",
                    "content": message,
                }
            ],
            model="gpt-3.5-turbo",
            max_tokens=150,  # Adjust response length
            temperature=0.7
        )
        return chat_completion.choices[0].message['content']
    
    except Exception as e:
        return f"Error: {str(e)}"
        

# if __name__ == "main":
#     user_message = "prompt"
#     ai_response = get_ai_response(user_message)
#     print(f"AI Response: {ai_response}")