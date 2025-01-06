
FROM python:3.9-slim


WORKDIR /frontend


COPY . /frontend


RUN pip install --no-cache-dir -r conditions.txt


EXPOSE 5000


ENV FLASK_APP=frontend.py
ENV FLASK_RUN_HOST=0.0.0.0


CMD ["flask", "run"]
