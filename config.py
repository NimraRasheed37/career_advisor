import os
from dotenv import load_dotenv, find_dotenv
from agents import AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig

# find and load .env file
load_dotenv(find_dotenv())

api_key = os.getenv("GEMINI_API_KEY")

# check the availibility of api key
if not api_key:
    raise ValurError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

# client info
external_client = AsyncOpenAI(
    api_key = api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# model info
model = OpenAIChatCompletionsModel(
    model= "gemini-2.0-flash",
    openai_client = external_client
)

gemini_config = RunConfig(
    model = model,
    model_provider = external_client,
    tracing_disabled = True
)