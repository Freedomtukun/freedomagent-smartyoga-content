# main.py
from crewai import Crew, Agent, Task
from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

# 定义智能体和任务
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

# 添加 Web 接口
@app.post("/generate")
async def generate(request: Request):
    result = crew.kickoff()
    return {"content": result}
