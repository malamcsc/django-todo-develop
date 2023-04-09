FROM python:alpine3.9
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN mkdir app
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN python /app/manage.py migrate

EXPOSE 8000
CMD [ "python", "/app/manage.py","runserver","0.0.0.0:8000"]

