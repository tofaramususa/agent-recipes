from together import Together
from dotenv import load_dotenv
from pathlib import Path


dotenv_path = Path('../.env')
load_dotenv(dotenv_path=dotenv_path)
client = Together();

def run_llm(user_prompt : str, model : str, system_prompt : str = None):
    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    
    messages.append({"role": "user", "content": user_prompt})
    
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.7,
        max_tokens=4000,        
    )

    return response.choices[0].message.content
