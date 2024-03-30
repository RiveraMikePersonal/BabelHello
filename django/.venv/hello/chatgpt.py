import openai
from hello.app.settings import *

#method to take two arguments feed it to openai for translation and return a response
def chat(language, content):
    print(language)
    print(content)
    openai.api_key = OPENAI_API_KEY
    completion = openai.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
          {"role": "user", "content": "Please translate the sentence after the colon into "+ language +" : "+content}
            #{"role": "user", "content": "Write a C# class for an object that has 3 properties an integer, a string, and a dictionary of int,string"}
        ]
    )
    return completion.choices[0].message.content