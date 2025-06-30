from crewai import Task
from agents.content_agent import content_agent

generate_post = Task(
    description='根据提示语创建一个瑜伽训练建议或训练序列',
    expected_output='一个结构化的训练建议段落',
    agent=content_agent
)
