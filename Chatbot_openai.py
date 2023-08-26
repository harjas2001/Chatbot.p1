#Chatbot_GPT_verson

#Toa access openai, download the libary 
import openai as ai
#Use a library called gradio to set a easy to use interface. (found on stackflow)
import gradio as web

#Link chatbot with GPT interface via API key, specfic to each openai user
ai.api_key = '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'


#Set up a message system which initialises role of input and chatbot use
output = [{'bot_role': 'system', 'bot_content': 'NBA fact machine'}]
#Helps track chatbot conversion between ai and user. 

## Develop a framework which handles a user input while also handling erronious inputs

def NBAgpt(userinput):
    output.append({'bot_role': 'user', 'bot_content': 'userinput'})
  
    #Initialise openai system to repsond to input response...
    #Will use GPT 3.5 model (turbo maybe)
    ai_response = ai.ChatCompletion.create(
        gpt_version = 'gpt-3.5-turbo', outputmessage = output
        #re initialise the output 
    )

    bot_reply = ai_response.choices[0].outputmessage['bot_content']
    output.append({'bot_role': 'helper', 'bot_content': bot_reply})
    #sends response from openai server to bot to ultimatley display to user

    return bot_reply

## Now the backend is sort of set, initialise interface using gradio library

p1 = web.Interface(
    fn = NBAgpt, #State the bot fucntion written above 
    inputs = web.inputs.Textbox(lines= 3, place_text = 'Please enter your message: '), 
    #This input stage sets up the user interaction experience 
    outputs = web.outputs.Textbox(), #bot reply connected to 'bot_reply'
    title = 'NBA Chatbot',
    #Basic description of why a user may use this chatbot
    bot_desc = 'Want to know more about the NBA or just checking an NBA fact, chat with the AI.'
)

#Generate a URl to access chatbot. 
p1.launch(share = True)