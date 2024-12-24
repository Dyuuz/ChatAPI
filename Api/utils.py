from openai import OpenAI
from django.conf import settings

def get_ai_response(message):
    try:
        client = OpenAI(api_key="settings.API_KEY")
        #openai.api_key = settings.API_KEY

        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {
                "role": "user",
                "content": message,
                }
            ],
            max_tokens=120,
        )
        return completion.choices[0].message.content
        #return completion['choices'][0]['message']['content']
    
    except Exception as e:
        return f"Error: {str(e)}"