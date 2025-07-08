# main.py
from crewai import Agent, Task, Crew

agent = Agent(
    role="Yoga Tip Generator",
    goal="生成一句瑜伽体式的练习建议",
    backstory="你是一位熟悉体式原理的中文瑜伽教练。",
)

task = Task(
    description="生成一句中文瑜伽提示",
    expected_output="一句带呼吸、觉知、身体感知的中文句子",
    agent=agent,
)

crew = Crew(
    agents=[agent],
    tasks=[task],
)

def run():
    return crew.kickoff()
