import os

# 读取 OpenAI API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("❌ Environment variable OPENAI_API_KEY not found. Please set it in CrewAI dashboard.")

# 配置项（可自定义）
DEFAULT_MODEL = "gpt-4o"
TEMPERATURE = 0.7
MAX_TOKENS = 2048

# 避免部署日志冲突，注释 debug 信息
# print(f"✅ Loaded config: model={DEFAULT_MODEL}, temperature={TEMPERATURE}")
