FROM python:3.8.10-slim-buster
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD python3 /app/docker_script.py
ENTRYPOINT ["python3","/app/docker_script.py"]