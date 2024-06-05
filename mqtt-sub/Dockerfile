FROM python:3.8

RUN apt-get update && \
    apt-get install -y cron && \
    apt-get install -y nano

WORKDIR /mqtt-sub

COPY . .

#ADD . /mqtt-sub

RUN /usr/local/bin/python -m pip install --upgrade pip

RUN pip --no-cache-dir install -r requirements.txt

ENV TZ=Asia/Taipei

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN chmod -R 777 /mqtt-sub/app

#CMD ['/usr/local/bin/python', '/mqtt-sub/app/sub-pzem-004t.py']
#ENTRYPOINT ["python", "/mqtt-sub/app/sub-pzem-004t.py"]
#CMD ['sh','run.sh']


