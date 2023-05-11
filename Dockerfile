FROM python:3.11

COPY requirements.txt requirements.txt

RUN python -m pip install --upgrade pip && pip install -r requirements.txt

WORKDIR /app

COPY main.py main.py
COPY dbwork.py dbwork.py
COPY settings.py settings.py

ENTRYPOINT ["python3", "main.py"]
