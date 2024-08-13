FROM python:3.11-slim

RUN mkdir /app
WORKDIR /app 

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY createTables.py .
COPY makeOrders.py .

COPY run.sh .
RUN chmod a+x run.sh

CMD ["./run.sh"]
#CMD ["tail","-f","/dev/null"]