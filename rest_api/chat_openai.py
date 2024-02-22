#
# REST API services to 
# 1. Directly talk to chatGPT/OpenAI
# 2. DIrectly talk to a CSV using chatGPT/OpenAI
#
# To run the REST API service run the following command
# $ uvicorn chat_openai:app --host 0.0.0.0 --port 8000 --reload
#
# REST APIs can be tested on the browser as well
#

import os
#from openai import OpenAI
import openai
from typing import Union
from fastapi import FastAPI

from langchain.agents.agent_types import AgentType
#from langchain_community.llms import OpenAI
from langchain_openai import OpenAI

from langchain_experimental.agents.agent_toolkits import create_csv_agent
from langchain_experimental.agents.agent_toolkits.csv.base import create_csv_agent

app = FastAPI()


client = openai.OpenAI(
  api_key=os.environ['OPENAI_API_KEY'],  # this is also the default, it can be omitted
)

MODEL = "gpt-3.5-turbo"
csv_file_name = "test.csv"


# Default REST API to display a message
@app.get("/")
def read_root():
    return {"Welcome": "You can now talk to chatGPT"}

# 
# This API connects to OpenAI and allows a bot to converse directly with chatGPT
#
# OpenAI REST API
# Usage: http://<server name/IP>/prompt/{user prompt}
#
@app.get("/prompt/{user_input}")
def read_input(user_input: str):
    response = client.chat.completions.create(
    model=MODEL,
    messages=[
        #{"role": "user", "content": "Explain asynchronous programming in the style of the pirate Blackbeard."},
        {"role": "user", "content": user_input},
    ],
    temperature=0,
)
    print(response)

    return {"response": response.choices[0].message.content}

#
# This API allows for talking with a CSV file
# The CSV file is being ingested within the API
# The file has to be named, test.csv, and placed in the same folder as this code
#
# OpenAI - langchain CSV REST API
# Usage: http://<server name/IP>/csv/{user prompt}
# 
@app.get("/csv/{user_question}")
def chat_csv(user_question: str, csv_file = csv_file_name):
    agent = create_csv_agent(OpenAI(temperature=0), csv_file, verbose=True, agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,)
    #response = f"{agent.run(user_input)}"
    #response = f"{agent.invoke(user_question)}"
    response = agent.invoke(user_question)

    # Extract the output from the response directory
    #output_val = response['output']
    
    return{"response": response['output']}
    
    

