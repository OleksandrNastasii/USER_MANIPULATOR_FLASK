FROM python:3.10-slim

WORKDIR /USER_MANIPULATOR_FLASK

ENV FLASK_APP=main.py

ENV FLASK_RUN_HOST=0.0.0.0

RUN apk add --no-cache gcc musl-dev linux-headers

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

EXPOSE 5000

COPY . .

CMD ["flask", "run", "--host=0.0.0.0"]