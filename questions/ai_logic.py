import os
import json
from dotenv import load_dotenv

def configure():
    load_dotenv()

configure()
endpoint = os.getenv("URLBASE")  
deployment = os.getenv("DEPLOYMENT_NAME", "gpt-35-turbo")  
subscription_key = os.getenv("KEYBASE")  


from openai import AzureOpenAI
def chatprocessor(ques , data , temparature , maxresponcelength):
    client = AzureOpenAI(  
    azure_endpoint=endpoint,  
    api_key=subscription_key,  
    api_version="2024-05-01-preview",  
    )
    chat_prompt = [
        {
            "role": "system",
            "content": "You are given this data . answer the question using information from given data"+" " + str(data)
        }
    ]


    role = "user" 
    chat_prompt.append({
        "role": role,
        "content": ques
    })
     
        
    messages = chat_prompt  
    completion = client.chat.completions.create(  
        model=deployment,  
        messages=messages,  
        max_tokens=min(int(maxresponcelength) , 120),  
        temperature=float(temparature),  
        top_p=0.95,  
        frequency_penalty=0,  
        presence_penalty=0,  
        stop=None,  
        stream=False
    )

    x = completion.to_json()
    y = json.loads(x)
    content = y['choices'][0]['message']['content']
    return content

def get_answer(q , d):
    s = chatprocessor(q , d , 0.7 , 100)
    print(q,d)
    return s

