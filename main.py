#!/bin/python
import os
import openai
from pathlib import Path
from dotenv import load_dotenv
load_dotenv(dotenv_path=Path('./personal_openai.env'))
openai.organization = os.getenv('OPENAI_ORGANIZATION')
openai.api_key = os.getenv('OPENAI_API_KEY')

system_role = 'Act as a highly intelligent assistant.'
prompt = 'Greetings!'

while prompt != 'exit':
    chat = openai.ChatCompletion.create(
        model='gpt-3.5-turbo', 
        messages=[
            {
                'role': 'system', 
                'content': system_role
            },
            {
                'role': 'user', 
                'content': prompt
            }])
    print('\nTermGPT: ', chat.choices[0].message.content)
    prompt = input('\n'+os.getlogin()+': ')