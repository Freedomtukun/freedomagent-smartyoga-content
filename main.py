from crewai import Crew, Agent, Task

agent = Agent(
    role="Yoga Content Creator",
    goal="Generate one-line yoga tip",
    backstory="Knows yoga & meditation.",
    verbose=True,
)

task = Task(
    description="输出一句瑜伽练习提示",
    expected_output="一句中文提示",
    agent=agent,
)

crew = Crew(agents=[agent], tasks=[task], verbose=True)

# ----- ① 供平台调用 -----
def run():
    result = crew.kickoff()
    print("✅ RESULT:", result)
    return result
