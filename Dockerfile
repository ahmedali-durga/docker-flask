FROM python:3.5
MAINTAINER ahmedali@codenation.co.in

RUN apt-get update && apt-get install -y --no-install-recommends python3-pip

ENV APP /var/app

ADD ./requirements.txt ${APP}/requirements.txt

RUN pip3 install -r ${APP}/requirements.txt

ADD . ${APP}

WORKDIR ${APP}

CMD python3 application.py