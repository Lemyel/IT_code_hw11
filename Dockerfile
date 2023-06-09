FROM python:3.10.4

COPY requirements.txt /tmp

RUN pip install -r /tmp/requirements.txt

COPY . /opt/app

WORKDIR /opt/app

CMD ["python", "manage.py", "runserver", "0:8000"]