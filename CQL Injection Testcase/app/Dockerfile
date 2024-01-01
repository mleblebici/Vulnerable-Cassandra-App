FROM python:3.8
WORKDIR /app
COPY . /app
RUN pip install flask cassandra-driver
RUN pip install cqlsh
EXPOSE 8000
ENV FLASK_APP app.py
COPY app-entrypoint.sh /app-entrypoint.sh
RUN chmod +x /app-entrypoint.sh
