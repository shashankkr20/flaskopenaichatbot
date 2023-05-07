import openai

openai.api_key="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"

# inputs="largest animal of planet"

def gpt_reply(input):

    # prompt to provide context for user input
    prompt = f"Please complete the following sentence: '{input}'"

    # Calling the OpenAI GPT-3 API to generate a response based on user prompt
    try:
        response = openai.Completion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": "'{prompt}'"}
            ]
        )
        message = response.choices[0].message.content
        return message
    except Exception as e:
        message = f"Error: {e}"
        return message