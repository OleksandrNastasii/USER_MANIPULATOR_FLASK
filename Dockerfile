FROM python:3.10-slim

WORKDIR /USER_MANIPULATOR_FLASK

COPY . /USER_MANIPULATOR_FLASK

RUN pip install -r requirements.txt

EXPOSE 5000

CMD python ./main.py