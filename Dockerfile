FROM python:3.11-slim
WORKDIR /app
COPY . /app
ENV PYTHONPATH=/app
RUN pip install --no-cache-dir crewai openai python-dotenv
CMD ["python", "-c", "import main; main.run()"]
