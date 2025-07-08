# main.py
from crewai import Agent, Task, Crew

# 定义智能体
agent = Agent(
    role="Yoga Content Creator",
    goal="Generate one-line yoga tip",
    backstory="Knows yoga & meditation.",
    verbose=True,
)

# 定义任务
task = Task(
    description="输出一句瑜伽练习提示",
    expected_output="一句中文提示",
    agent=agent,
)

# 创建 Crew
crew = Crew(
    agents=[agent],
    tasks=[task],
    verbose=True,
)

# CrewAI 自动调用这个函数
def run():
    return crew.kickoff()
