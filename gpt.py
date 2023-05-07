import openai

import os

openai.api_key=os.environ.get('OPENAI_API_KEY')

# inputs="largest animal of planet"

def gpt_reply(input):

 

    # Calling the OpenAI GPT-3 API to generate a response based on user prompt
    try:
        response = openai.Completion.create(
            engine="davinci",
            prompt=input,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.7
        )
        if response and len(response.choices) > 0:
            return response.choices[0].text
        else:
            return None
    except Exception as e:
        raise ValueError("Failed to generate text: " + str(e))