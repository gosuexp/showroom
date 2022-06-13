FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR .

COPY requirements.txt .

RUN python3 -m pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000




