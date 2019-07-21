FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache -r requirements.txt

COPY * ./

CMD [ "python", "./test_send_postcard.py" ]
