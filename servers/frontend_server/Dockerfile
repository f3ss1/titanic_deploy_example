FROM python:3.10-slim
EXPOSE 8501
WORKDIR app
RUN pip install --no-cache streamlit

COPY servers/frontend_server /app/frontend_server

ENTRYPOINT ["streamlit", "run", "frontend_server/streamlit_server.py"]