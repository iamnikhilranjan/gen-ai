from dotenv import load_dotenv
from openai import OpenAI

import json
load_dotenv()

client = OpenAI()

def get_weather(city: str):
    #TODO! : do an actual API call
    return "32 degree celcius"

available_tools = {
    "get_weather" : {
        "fn" : get_weather,
        "description" : "Takes the city name as input and return the current weather of the city"
    }
}

system_prompt = '''
   You are an helpful AI assistant who is specialized in resolving user querry. 
   You work on start , plan, action, observe mode.
   for the given user query and availanbel tools, plan the step by step execution, based on the planning, select the relevant tool from the available tool. and based on the tool selection you perform an action to call the tool. Wait for the observation and based on the obdervation from the tool call resolve the user querry. 

   Rules: 
   - Follow the output JSON format.
   - Always perform one step at a time and wait for the next input.
   - Carefully analyse the user query.

   Output JSON Format: 
   {{
     "step": "string",
     "content": "string",
     "function": "The name of function if the step is action",
     "input": "The input parameter fot the function"
   }}

   Available Tools: 

   Example: 
   User Query: What is the user of new York ?
   Output: {{"step": "plan", "content": "The user is interested in weather data of new york"}}
   Output: {{"step": "plan", "content": "From the available tools I should call get_weather"}}
   Output: {{"step": "action", "function": "get_weather", "input": "new york"}}
   Output: {{"step": "observe", "output": "12 Degree cel"}}
   Output: {{"step": "output", "content": "The weather for new york seems to be 12 degrees."}}


'''

messages = [
    {"role": "system", "content": system_prompt}
]

user_query = input('> ')
messages.append({"role": "user", "content": user_query})

while True: 
    response = client.chat.completions.create(
        model = "gpt-4o",
        response_format={"type": "json_object"},
        messages = messages
    )

    parsed_ouput = json.loads(response.choices[0].message.content)
    messages.append({"role": "assistant", "content": json.dumps(parsed_ouput)})

    if parsed_ouput.get("step") == "plan": 
        print(f"brain: {parsed_ouput.get("content")}")
        continue

    if parsed_ouput.get("step") == "action":
        tool_name = parsed_ouput.get("function")
        tool_input = parsed_ouput.get("input")

        if available_tools.get(tool_name, False) != False:
            available_tools[tool_name].get("fn")(tool_input)


response = client.chat.completions.create(
    model = "gpt-4o",
    response_format={"type": "json_object"},
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": "what is the current weather of Patyala?"},
        {"role": "assistant", "content": json.dumps({"step": "plan", "content": "The user is asking for current weather in Patiala"})},
        {"role": "assistant", "content": json.dumps({"step": "plan", "content": "From the available tools, I should call get_weather to obtain the weather information for patiala."})},
        {"role": "assistant", "content": json.dumps({"step": "action", "Function": "grt_weather", "input": "Patiala"})},
        {"role": "assistant", "content": json.dumps({"step": "observe", "output": "32 degree celcius!"})},
    ]
)

print(response.choices[0].message.content)