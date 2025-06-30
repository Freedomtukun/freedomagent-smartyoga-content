# src/config/config.py

import os

# 从环境变量读取 OpenAI API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# 如果没有设置，抛出错误
if not OPENAI_API_KEY:
    raise ValueError("❌ 未找到 OPENAI_API_KEY，请在 CrewAI 平台的 Environment Variables 中设置。")

# 可选：指定默认模型和其他配置（你可以根据需要扩展）
DEFAULT_MODEL = "gpt-4o"
TEMPERATURE = 0.7
MAX_TOKENS = 2048

# 日志或调试用途
print(f"✅ 已加载配置，模型: {DEFAULT_MODEL}，温度: {TEMPERATURE}")
