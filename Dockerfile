FROM python:3.9
WORKDIR /app
COPY . /app
RUN pip3 install --upgrade pip && pip install --no-cache-dir -r requirements.txt
ENV FLASK_APP=app
CMD ["python","app.py"]