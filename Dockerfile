FROM continuumio/miniconda3

RUN apt-get update && \
        apt-get install -y python3 && \
        apt-get install -y python3-pip && \
        apt-get install -y build-essential

RUN mkdir /opt/src
COPY ./src /opt/src
WORKDIR /opt/src
ADD requirements.txt /opt/src/

RUN ["conda", "create", "-n", "code2cloud", "python=3.6"]

RUN /bin/bash -c "source activate code2cloud && pip install --trusted-host pypi.python.org -r /opt/src/requirements.txt"

# deploy environments: dev, stage, prod
ENV AWS_DEPLOY_ENV=dev

# PostgreSQL DB params: via os env, docker run env, or Vault secrets
ENV AWS_PG_DB_NAME=traffic_db
ENV AWS_PG_DB_HOST=
ENV AWS_PG_DB_USER=
ENV AWS_PG_DB_PASS=

CMD /bin/bash -c "source activate code2cloud && python /opt/src/dash/app.py"
