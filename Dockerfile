FROM python:3.8-bullseye
EXPOSE 8000
COPY . .
CMD ["pip", "install", "requirements.txt"]
RUN "uvicorn main:app"
