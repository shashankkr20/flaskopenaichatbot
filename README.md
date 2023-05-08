
# Flask Web Application with OpenAI Chatbot Integration

The purpose of this project is to provide a web application that uses the Flask framework and OpenAI's GPT-3 API to offer chatbot functionality. The application's main features include a homepage with a form that accepts user input for a prompt or question, a results page that displays the chatbot's response, and error handling for API errors or failed requests.



## SETUP & INSTALLATION

Clone the repository to your local machine using git clone https://github.com/pandiji/flaskopenaichatbot.git.

Create a virtual environment and activate it using python3 -m venv env and source env/bin/activate respectively.

Install the required dependencies using pip install -r requirements.txt.

Set the OpenAI API credentials as environment variables (e.g., export OPENAI_SECRET_KEY=<your-secret-key> and export OPENAI_API_KEY=<your-api-key>).

Run the application using flask run
## API CALLS AND RESPONSES

1. First of all we make a python file called ‘gpt.py’ which has a function called gpt_reply which performs the api call and generate the response which we store in message variable.Below you can see we have provided context to user query.

import openai

openai.api_key = "YOUR_API_KEY_HERE“

def gpt_reply(input):

  
prompt to provide context for user input
prompt = f"Please complete the following sentence: '{input}'"

2) To make a request to the OpenAI API, the application uses the openai.Completion.create method from the openai Python package. This method takes several parameters, including the API key, the model ID, the prompt, and the number of tokens to generate.
The response from the OpenAI API is a JSON object that contains the generated text, along with metadata like the time taken to generate the response and any warnings or errors. The generated text can be accessed using the response.choices[0].message.content attribute.
.

Calling the OpenAI GPT-3 API to generate a response based on user prompt 

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

## ROUTES AND CONTROLLERS

HOME PAGE:

The home page (/) displays a simple form that accepts user input for a prompt or question. When the form is submitted, the application makes a request to the OpenAI API to generate a response based on the user's input. The response is then displayed on the results page.

@app.route("/",methods=["POST","GET"])

RESULT PAGE:

After a user submitted a prompt or question through the web application's homepage, the server-side Flask code would make a call to the OpenAI GPT API function in ‘gpt.py’ file which is imported in ‘app.py’ using the user's input as the prompt. The GPT API would then generate a response based on the input and return it to the Flask application as a string.

The Flask application would then render the result page with the generated response included as part of the page content. The result page would display the response in a formatted and readable way, allowing the user to easily view and interpret the chatbot's output.

Overall, the result page was a critical component of the chatbot project, as it was the primary means by which users could interact with the chatbot and receive intelligent and contextual responses to their prompts.



@app.route("/<result>")
def result(result):
        return render_template('result.html',prompt=result)


## Screenshots

![Request](/photo/login.png)

![Response](/photo/home.png)
