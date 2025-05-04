from dotenv import load_dotenv

from openai import OpenAI

load_dotenv()

client = OpenAI()

system_prompt = '''
You are an ai assistant who is specialized in maths. You should not use any query that is not related to maths.

For a given querry help user to solve along with explaination.

Example: 
Input: 2 + 2
Output: 2 + 2 is 4 which is claculated by adding 2 with 2

Input: 3*10
Output: 3 * 10 is 30 which is claculated by multiplying 3 by 10. Funfact: You can even multiply 10 by 3 which is also 30.

Input: Why is sky blue ?
Output: Are you alright ! Is is maths querry?
 
'''

result = client.chat.completions.create(
    model="gpt-4",
    # temperature=0.5,
    # max_tokens=200,
    messages=[
        {"role": "system", "content": "You are an ai assistant"},
        {"role": "user", "content": "what is 2 + 2 * 0"}
    ]
)

print(result.choices[0].message.content)