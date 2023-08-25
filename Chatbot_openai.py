#Chatbot_GPT_verson

#Toa access openai, download the libary 
import openai as ai
#Use a library called gradio to set a easy to use interface. (found on stackflow)
import gradio as web

#Link chatbot with GPT interface via API key
ai.api_key = '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'


#Set up a message system which initialises role of input and chatbot use
output = [{'bot_role': 'system', 'bot_content': 'NBA fact machine'}]

## Develop a framework which handles a user input while also handling erronious inputs

def NBAgpt(userinput):
    output.append({'bot_role': 'user', 'bot_content': 'userinput'})
  
    #Initialise openai system to repsond to input response...
    #Will use GPT 3.5 model (turbo maybe)
    ai_response = ai.ChatCompletion.create(
        gpt_version = 'gpt-3.5-turbo', output = output
        #re initialise the output 
    )

    reply = output['choices'][0]['message']['bot_content']
    output.append({'bot_role': 'helper', 'bot_content': reply})

    return reply

## Now the backend is sort of set, initialise interface using gradio library

p1 = web.Interface(fn = NBAgpt, inputs = 'text', outputs = 'text', title = 'NBA fan ')

p1.launch(share = True)