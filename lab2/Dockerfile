FROM python:3-slim-bullseye

RUN apt update && apt install -y iputils-ping
RUN pip install validators
COPY main.py main.py

ENTRYPOINT ["python", "main.py"]
