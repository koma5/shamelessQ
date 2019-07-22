FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache -r requirements.txt

COPY * ./

CMD [ "python", "-u", "./send_postcard.py" ]
