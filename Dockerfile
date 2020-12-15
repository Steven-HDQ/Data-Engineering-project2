FROM python:3.6

WORKDIR /app

ENV FLASK_APP=app.py

COPY requirements.txt .

RUN pip install -i https://pypi.douban.com/simple/ -r requirements.txt 

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]