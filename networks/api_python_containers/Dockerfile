FROM python:3

RUN apt-get update -y && \
  apt-get install -y  python3-pip python-dev-is-python3

WORKDIR /app


RUN pip install requests Flask flask_sqlalchemy


COPY . .

EXPOSE 5001

CMD [ "python", "./app.py" ]