import os
from dotenv import load_dotenv
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, set_tracing_disabled, RunContextWrapper, function_tool
import rich
from pydantic import BaseModel

load_dotenv()
set_tracing_disabled(disabled=True)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

class User_Info(BaseModel):
    name: str
    age: int
    alive: bool
    roll_no: str

my_info = User_Info(name = "Nida", age = 23, alive = True, roll_no = "abc12345000")    


def dynamic_ins(wrapper: RunContextWrapper[User_Info], agent:Agent):
    wrapper.context.name = "Linta"
    return f"whenever user ask for a roll_no  or name you use given tool user information to get roll_no of their user, user name is {wrapper.context.name} and user age is {wrapper.context.age} " 

@function_tool
async def User_information(wrapper: RunContextWrapper[User_Info]):
    
    return f"user roll no is {wrapper.context.roll_no} and user name is {wrapper.context.name}"


client = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

agent = Agent[User_Info](
    name = "triage_agent",
    instructions= dynamic_ins,
    model = OpenAIChatCompletionsModel(model= "gemini-2.0-flash", openai_client= client),
    tools= [User_information]
)

result = Runner.run_sync(agent, "what is the name of user? and what his roll no?", context=my_info)
rich.print(result.final_output)