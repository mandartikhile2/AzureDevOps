FROM python:3.8
WORKDIR /app 
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 80
CMD python ./start_ai_preprocessing.py

COPY requirements.txt /app/requirements.txt
ENTRYPOINT ["python", "./start_ai_preprocessing.py"]
