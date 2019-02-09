FROM python:3.6-alpine

RUN python -m venv code2cloud
RUN source code2cloud/bin/activate

RUN mkdir /opt/src
COPY ./src /opt/src
WORKDIR /opt/src
ADD requirements.txt /opt/src/
RUN pip install -r requirements.txt

CMD ["python", "/opt/src/dash/app.py"]

