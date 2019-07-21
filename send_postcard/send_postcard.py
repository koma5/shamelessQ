from postcard_creator.postcard_creator import PostcardCreator, Postcard, Token, Recipient, Sender
import schedule, time, json, requests, os

couchdb_database = 'http://192.168.1.3:5984/postcards/'

def run():
    token = login()
    postcard_data = get_next_postcard()
    picture = get_postcard_picture(postcard_data)
    postcard = create_postcard(postcard_data, picture)
    try:
        send_postcard(postcard, token)
    except Exception as e:
        if ("Limit of free postcards exceeded." in str(e)):
            handle_cooldown(e)
        else:
            print(e)

def handle_cooldown(e):
    print(e, "le'me schedule and come back, okay?")

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
    response = requests.post(couchdb_database + '_find', headers={"content-type":"application/json"}, data=data)
    result = json.loads(response.content.decode('utf-8'))
    return result['docs'][0]

def get_postcard_picture(postcard):
    attachment_id = list(postcard['_attachments'].keys())[0]
    response = requests.get(couchdb_database + postcard['_id'] + '/' + attachment_id)
    return response.content


schedule.every(10).seconds.do(run)
run()

while True:
    schedule.run_pending()
    time.sleep(1)
