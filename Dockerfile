FROM python:3.7

RUN apt update 
RUN apt install -y libgl1-mesa-glx

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip --default-timeout=100 install -r requirements.txt

COPY . /app

EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]