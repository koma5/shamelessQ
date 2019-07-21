FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache -r requirements.txt

COPY * ./

CMD [ "python", "./send_postcard.py" ]
