FROM python:3.8-slim-buster

RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    gcc && \
    pip install --upgrade pip \
    pip install pipenv

COPY ./ /app/

WORKDIR /app

RUN pipenv install -e .

EXPOSE 5000

CMD ["pipenv", "run", "python", "flask_boiler/main.py"]
