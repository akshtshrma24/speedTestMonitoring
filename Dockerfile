FROM python:3.10.1

WORKDIR /internetMonitoring

EXPOSE 8000

RUN pip3 install requests

COPY . . 

CMD ["python3", "metrics.py"]