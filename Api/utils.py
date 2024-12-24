import time
from openai import OpenAI
import os
#from django.conf import settings

def get_ai_response(message):
    try:
        client = OpenAI(api_key=settings.API_KEY)
        #openai.api_key = settings.API_KEY

        completion = client.chat.completions.create(
            model="gpt-4",
            messages=[
                 {"role": "system", "content": "You are a helpful assistant."},
                 {
                   "role": "user",
                   "content": message,
                 }
            ],
        )
        return completion.choices[0].message.content
        #return completion['choices'][0]['message']['content']
    
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "main":
     user_message = "prompt"
     ai_response = get_ai_response(user_message)
     print(f"AI Response: {ai_response}")
