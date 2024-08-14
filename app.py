import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from langchain_altero.messages import stream_response

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("Did not find openai_api_key, please add an environment variable `OPENAI_API_KEY` which contains it, or pass `openai_api_key` as a named parameter.")

llm = ChatOpenAI(
    temperature=0.1,
    model_name="gpt-4o-mini",
    api_key=api_key
)

answer = llm.stream("Beritahu kami 10 tempat paling indah untuk dikunjungi di Indonesia dan alamatnya!")

stream_response(answer)