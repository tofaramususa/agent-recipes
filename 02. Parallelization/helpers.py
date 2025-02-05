import asyncio
import together
from together import AsyncTogether, Together

client = Together()

async_client = AsyncTogether()

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


#The function below will call the reference LLMs in parallel
async def run_llm_parallel(user_prompt: str, model : str, system_prompt : str = None):
    """Run a single LLM call with a reference model """
    for sleep_time in [1, 2, 4]:
        try:
            messages = []
            if system_prompt:
                messages.append({"role": "system", "content": system_prompt})
            messages.append({"role": "user", "content" : user_prompt})
            response = await async_client.chat.completions.create(
                    model=model,
                    messages=messages,
                    temperature=0.7,
                    max_tokens=2000,        
            )
            break
        except together.error.RateLimitError as e:
            print(e)
            await asyncio.sleep(sleep_time)
    return response.choices[0].message.content