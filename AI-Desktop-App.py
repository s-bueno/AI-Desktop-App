import openai

# Importing the OpenAI library 

# Setting the API key for openai, this key is used to authenticate your requests to the OpenAI API
openai.api_key = "YOUR API KEY"

def ask():
    # Prompting the user to input a question, the question is assigned to the variable 'prompt'
    prompt = input('How can I help?')
    
    # Checking if user input is 'q'
    # If the input is 'q', the function exits
    if prompt == "q":
        return
   
    # Setting the model to be used, in this case it's 'text-davinci-003'
    model = "text-davinci-003"

    # Using OpenAI's Completion.create() function to generate a response to the prompt
    # The function takes in 4 parameters
    # engine: model to be used
    # prompt: user input
    # max_tokens: maximum number of tokens to generate
    # temperature : controls the creativity of the response, 0 for no creativity and 1 for max creativity
    completion = openai.Completion.create(engine=model, prompt=prompt, max_tokens=1024, temperature=0.5)
    # returns the first value in the list created by the choices property as text 
    text = completion.choices[0].text
    
    # Printing the generated text
    print(text)
    # calling the function again, thus creating a loop that allows the user to continuously ask questions and receive responses
    ask()

#Initial call to the function to start the loop
ask()
