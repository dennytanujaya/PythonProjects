import google.generativeai as genai
import os

os.environ["API_KEY"] = 'GOOGLE_GEMINI_API_KEY'
genai.configure(api_key=os.environ["API_KEY"])

# Model Configuration
#model_config = {  "temperature": 1,"top_p": 0.99,"top_k": 0,"max_output_tokens": 4096}

#model = genai.GenerativeModel('gemini-1.5-pro-latest', generation_config=model_config)

# without fine tunning 
# model = genai.GenerativeModel('gemini-1.5-pro-latest')
#response = model.generate_content("President of Indonesia is")
#print(response.text)
#response = model.generate_content("the most efficient way to remove duplicates of a list in python. Less verbose response.")
#print(response.text)

#chat = model.start_chat(history=[])
#response = chat.send_message("2+2")
#print(response.text)
# Output
# 2 + 2 = 4

#response = chat.send_message("square of it")
#print(response.text)
# Output
# The square of 4 is 16

#response = chat.send_message("Add 4 to it")
#print(response.text)
# Output
# Adding 4 to 16 gives us 20.

#  Print list of Google Gemini AI Models
for model in genai.list_models():
    print(model.name)