from typing import List
from helpers import run_llm 

def serial_chain_workflow(input_query: str, prompt_chain : List[str]) -> List[str]:
    """Run a serial chain of LLM calls to address the `input_query` 
    using a list of prompts specified in `prompt_chain`.
    """
    response_chain = []
    response = input_query
    for i, prompt in enumerate(prompt_chain):
        print(f"Step {i+1}")
        response = run_llm(f"{prompt}\nInput:\n{response}", model='meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo')
        response_chain.append(response)
        print(f"{response}\n")
    return response_chain

# Example
question = "Sally earns $12 an hour for babysitting. Yesterday, she just did 50 minutes of babysitting. How much did she earn?"

prompt_chain = ["""Given the math problem, ONLY extract any relevant numerical information and how it can be used.""",
                """Given the numberical information extracted, ONLY express the steps you would take to solve the problem.""",
                """Given the steps, express the final answer to the problem."""]



def main():
    responses = serial_chain_workflow(question, prompt_chain)
    final_answer = responses[-1]



if __name__ == "__main__":
    main()
