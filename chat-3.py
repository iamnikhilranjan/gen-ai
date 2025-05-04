from dotenv import load_dotenv

from openai import OpenAI

load_dotenv()

client = OpenAI()

system_prompt = """
You are an i assistant who is expert in breaking down complex problems and then resolve the user querry.

For the given user input, analyse the input and break down the problem step by step. At least think 5-6 steps on how to solve th problem before solving it down.

This steps are you get a user input, you think, you again think for several times and then return an output with explaination and finally you validate the output as well before giving final result.

Follow these steps in sequence that is "analyse", "think", "output", "validate" and finally "result".

Rules: 
1. Follow the strict JSON output as per output schema.
2. Always perform one step at a time ans wait for the next input.
3. Carefully analyse the user querry.

Output format: 
{{step: "string", content: "string"}}

Example:
Input: what is 2 + 2 ?
Output: {{step: "Analyse", content: "Alright! The user is interested in maths qerry ans he is asking a basic arithematic operation"}}

Output: {{step: "think", content: "To perform the addition I must go from left to right and add all the operands"}}

Output: {{step: "Output", content: "$"}}

Output: {{step:"validate", content: "seems like 4 is correct answer for 2 + 2"}}

Output: {{step: "result}, content: "2 + 2 is = 4 and that is calculated by adding all numbers"}

"""

result = client.chat.completions.create(
    model="gpt-4o",
    response_format={"type": "json_object"},
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": "What is 3 + 4 * 5"},

        #
        
    ]
)

print(result.choices[0].message.content)





