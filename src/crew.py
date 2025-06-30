from crewai import Crew, Agent, Task
from crewai.tools import tool

@tool
def say_hi_tool(name: str) -> str:
    return f"Hi {name}, welcome to SmartYoga!"

agent = Agent(
    role='Yoga Content Assistant',
    goal='Help generate personalized yoga session content',
    tools=[say_hi_tool],
    verbose=True
)

task = Task(
    description='Say hello to a user named Alice',
    expected_output='Hi Alice, welcome to SmartYoga!',
    agent=agent
)

crew = Crew(
    agents=[agent],
    tasks=[task],
    verbose=True
)
