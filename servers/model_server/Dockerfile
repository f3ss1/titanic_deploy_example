FROM python:3.10-slim
EXPOSE 8000
WORKDIR app
RUN pip install --no-cache fastapi pandas uvicorn scikit-learn catboost

COPY models /app/models
COPY servers/model_server /app/model_server
COPY src /app/src

ENTRYPOINT ["uvicorn", "model_server.server:app", "--host", "0.0.0.0"]