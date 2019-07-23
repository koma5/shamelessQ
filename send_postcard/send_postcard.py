from postcard_creator.postcard_creator import PostcardCreator, Postcard, Token, Recipient, Sender
import schedule, time, re, json, requests, os
from io import BytesIO

couchdb_database = 'http://192.168.1.3:5984/postcards/'
couchdb_auth=(os.environ['COUCHDBUSER'], os.environ['COUCHDBPASSWORD'])

os.environ['TZ'] = 'UTC'
time.tzset()
print("setting timezone to UTC: " + time.strftime('%H:%M:%S%z'))

def run():
    token = login()
    postcard_data = get_next_postcard()
    picture = get_postcard_picture(postcard_data)
    postcard = create_postcard(postcard_data, picture)
    try:
        send_postcard(postcard, token)
        schedule.clear('run')
        print(schedule.every().day.at(time.strftime('%H:%M:%S')).do(run).tag('run'))
        mark_postcard_as_posted(postcard_data)
    except Exception as e:
        if ("Limit of free postcards exceeded." in str(e)):
            handle_cooldown(e)
        else:
            print(e)


def handle_cooldown(e):
    time_string = re.findall(r"([0-9]{2}:[0-9]{2}:[0-9]{2})", str(e))[0]
    print(e, "le'me schedule and come back, okay?")
    schedule.clear('run')
    print(schedule.every().day.at(time_string).do(run).tag('run'))

def login():
    token = Token()
    token.fetch_token(username=os.environ['POSTUSER'], password=os.environ['POSTPASSWORD'])
    token.has_valid_credentials(username=os.environ['POSTUSER'], password=os.environ['POSTPASSWORD'])
    return token

def send_postcard(postcard, token, mock=False):
    w = PostcardCreator(token)
    w.send_free_card(postcard=postcard, mock_send=mock)

def create_postcard(postcard, picture):

    rec = postcard['recipient']
    recipient = Recipient(
        prename=rec['firstname'],
        lastname=rec['lastname'],
        street=rec['address'],
        place=rec['city'],
        zip_code=rec['postcode'])

    sen = postcard['sender']
    sender = Sender(
            prename=sen['firstname'],
            lastname=sen['lastname'],
            street=sen['address'],
            place=sen['city'],
            zip_code=sen['postcode'])

    card = Postcard(message=postcard['message'],
            recipient=recipient,
            sender=sender,
            picture_stream=picture)

    return card

def get_next_postcard():
    data = json.dumps({"selector": {"posted":False}})
    response = requests.post(couchdb_database + '_find', headers={"content-type":"application/json"}, data=data, auth=couchdb_auth)
    result = json.loads(response.content.decode('utf-8'))
    return result['docs'][0]

def get_postcard_picture(postcard):
    attachment_id = list(postcard['_attachments'].keys())[0]
    response = requests.get(couchdb_database + postcard['_id'] + '/' + attachment_id, auth=couchdb_auth)
    return BytesIO(response.content)

def mark_postcard_as_posted(postcard):
    print(postcard)
    postcard['posted'] = True
    data = json.dumps(postcard)
    response = requests.put(couchdb_database + postcard['_id'], headers={"content-type":"application/json"}, data=data, auth=couchdb_auth)
    print(response)


run()

while True:
    schedule.run_pending()
    time.sleep(1)
