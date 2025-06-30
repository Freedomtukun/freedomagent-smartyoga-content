from crewai import Crew, Agent, Task

# 定义智能体
content_agent = Agent(
    role="瑜伽内容创作者",
    goal="为 SmartYoga 平台用户生成每日瑜伽引导内容",
    backstory="你是一个具备深厚瑜伽知识、热爱冥想的中文内容专家，懂得结合季节、节气、情绪等因素生成合适的文案。",
    verbose=True,
    allow_delegation=False,
)

# 定义任务
content_task = Task(
    description="为初学者生成一篇今日练习建议，包含体式推荐、引导语、建议练习时间。",
    expected_output="一段约300字的中文练习建议内容",
    agent=content_agent,
)

# 创建 Crew
crew = Crew(
    agents=[content_agent],
    tasks=[content_task],
    verbose=True
)

# ✅ 提供平台入口函数
def run():
    result = crew.kickoff()
    print("✅ 执行结果如下：")
    print(result)
    return result

# 本地调试入口
if __name__ == "__main__":
    run()
