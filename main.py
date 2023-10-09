import pandas as pd
import pandasql as pds
import re
from langchain.chat_models import AzureChatOpenAI
from prompts import dataPrompt

LLM_KEY = ""
LLM_DEPLOYMENT_NAME = ""
LLM_BASE = ""
LLM_VERSION = ""
LLM_MODEL = ""
DATA_DF = pd.read_csv("./data/ml_project1_data.csv")
LLM = AzureChatOpenAI(deployment_name=LLM_DEPLOYMENT_NAME, model_name=LLM_MODEL, openai_api_base=LLM_BASE, openai_api_key=LLM_KEY, openai_api_version=LLM_VERSION, verbose=False, cache=False)

def main():
    inquiry = input("What is your query?\n")
    prompt = dataPrompt.format(inquiry=inquiry)
    response = LLM.predict(prompt)
    try:
        #print(response)
        sqlquery = extract_code_from_string(response)[0]
        #print(DATA_DF)
        result = pds.sqldf(sqlquery, {'data_df':DATA_DF})
        print(result)
    except:
        print(response)

def extract_code_from_string(input_string):
    raw_code_blocks = re.findall(r'```(.*?)```', input_string, re.DOTALL)
    code_blocks = [block.split('\n', 1)[1] if '\n' in block else '' for block in raw_code_blocks]
    return [block.replace('\n', ' ') for block in code_blocks]

if __name__ == "__main__":
    while True:
        main()