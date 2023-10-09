This project requires a Azure OpenAI chatgpt deployment.
1. Create a python virtual environment.
2. Install all the python packages in the requirements.txt file to the virtual environment.
3. Fill out the variables at the top of the python file with the required information (Specified below).
4. Activate the python environment.
5. Run main.py.

Required variables:
- LLM_KEY = OpenAI Resource Key
- LLM_DEPLOYMENT_NAME = OpenAI model deployment name
- LLM_BASE = Base URL for OpenAI resource
- LLM_VERSION = The version of the model. You may need to go to the Azure OpenAI Studio chat playground and check the sample code for this.
- LLM_MODEL = The LLM model e.g. gpt-4
