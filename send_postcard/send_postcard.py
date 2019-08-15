# -*- coding: utf-8 -*-
from postcard_creator.postcard_creator import PostcardCreator, Postcard, Token, Recipient, Sender, PostcardCreatorException
import schedule, time, re, json, requests, os
from io import BytesIO

couchdb_database = os.environ['COUCHDBURL']
couchdb_auth=(os.environ['COUCHDBUSER'], os.environ['COUCHDBPASSWORD'])

safety_delay = 0

os.environ['TZ'] = 'UTC'
time.tzset()
print("setting timezone to UTC: " + time.strftime('%H:%M:%S%z'))

def run():
    global safety_delay
    postcard_data = get_next_postcard()
    picture = get_postcard_picture(postcard_data)
    postcard = create_postcard(postcard_data, picture)
    token = login()
    time.sleep(safety_delay)
    try:
        response = send_postcard(postcard, token)
        print(response)
        schedule.clear('run')
        next_run = time.strftime('%H:%M:%S')
        schedule.every().day.at(next_run).do(run).tag('run')
        print("next: ", next_run)
        mark_postcard_as_posted(postcard_data)
    except PostcardCreatorException as e:
        if ("Limit of free postcards exceeded." in str(e)):
            handle_cooldown(e)
        else:
            print(e)

    safety_delay = 33




def handle_cooldown(e):
    time_string = re.findall(r"([0-9]{2}:[0-9]{2}:[0-9]{2})", str(e))[0]
    print(e, "le'me schedule and come back, okay?")
    schedule.clear('run')
    schedule.every().day.at(time_string).do(run).tag('run')
    print("next: ", time_string)

def login():
    token = Token()
    token.fetch_token(username=os.environ['POSTUSER'], password=os.environ['POSTPASSWORD'])
    token.has_valid_credentials(username=os.environ['POSTUSER'], password=os.environ['POSTPASSWORD'])
    return token

def send_postcard(postcard, token, mock=False):
    print('send postcard')
    w = PostcardCreator(token)
    return w.send_free_card(postcard=postcard, mock_send=mock)

def create_postcard(postcard, picture):

    rec = postcard['recipient']
    company = rec['company'] if ('company' in rec.keys()) else ''
    company_addition = rec['company_addition'] if ('company_addition' in rec.keys()) else ''
    salutation = rec['salutation'] if ('salutation' in rec.keys()) else ''

    recipient = Recipient(
        company=company,
        company_addition=company_addition,
        salutation=salutation,
        prename=rec['firstname'],
        lastname=rec['lastname'],
        street=rec['address'],
        place=rec['city'],
        zip_code=rec['postcode'])

    sen = postcard['sender']
    del company
    company = sen['company'] if ('company' in sen.keys()) else ''

    sender = Sender(
            company=company,
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
    data = json.dumps({"selector": {"posted":False}, "sort":[{"order": "asc"}]})
    response = requests.post(couchdb_database + '_find', headers={"content-type":"application/json"}, data=data, auth=couchdb_auth)
    result = json.loads(response.content.decode('utf-8'))
    if response.status_code != 200:
        print(result)
    try:
        return result['docs'][0]
    except IndexError:
        print("Queue is empty. Shame on you, queue should never be empty!!")
        time.sleep(60)
        quit(1)


def get_postcard_picture(postcard):
    attachment_id = list(postcard['_attachments'].keys())[0]
    response = requests.get(couchdb_database + postcard['_id'] + '/' + attachment_id, auth=couchdb_auth)
    return BytesIO(response.content)

def mark_postcard_as_posted(postcard):
    print("timestamp posted postcard")
    print(postcard)
    postcard['posted'] = time.strftime('%FT%TZ')
    data = json.dumps(postcard)
    response = requests.put(couchdb_database + postcard['_id'], headers={"content-type":"application/json"}, data=data, auth=couchdb_auth)
    print(response)


run()

while True:
    schedule.run_pending()
    time.sleep(1)
