FROM python:3.9# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR .

COPY requirements.txt .

RUN python3 -m pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000




