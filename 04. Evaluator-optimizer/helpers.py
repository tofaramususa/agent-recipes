import json
from pydantic import ValidationError
from together import Together

client = Together()

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

def JSON_llm(user_prompt : str, schema, system_prompt : str = None):
    try:
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
    
        messages.append({"role": "user", "content": user_prompt})
        
        extract = client.chat.completions.create(
            messages=messages,
            model="meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo",
            response_format={
                "type": "json_object",
                "schema": schema.model_json_schema(),
            },
        )
        return json.loads(extract.choices[0].message.content)

    except ValidationError as e:
        error_message = f"Failed to parse JSON: {e}"
        print(error_message)