FROM python:3.8
EXPOSE 8000
COPY . .
#RUN "py -m pip install -r requirements.txt"
#RUN "pip install -r requirements.txt"
#CMD ["pip", "install", "-r", "requirements.txt"]
RUN pip install -r requirements.txt
CMD ["uvicorn" , "main:app" , "--host", "0.0.0.0", "--port", "8000"]
