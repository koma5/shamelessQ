from postcard_creator.postcard_creator import PostcardCreator, Postcard, Token, Recipient, Sender

import os

token = Token()
token.fetch_token(username=os.environ['POSTUSER'], password=os.environ['POSTPASSWORD'])
token.has_valid_credentials(username=os.environ['POSTUSER'], password=os.environ['POSTPASSWORD'])

recipient = Recipient(prename='Marco', lastname='Koch', street='Niederwies 18', place='Vorderthal', zip_code=8857)

sender = Sender(prename='Marco', lastname='Koch', street='Niederwies 18', place='Vorderthal', zip_code=8857)

card = Postcard(message='test', recipient=recipient, sender=sender, picture_stream=open('./my-photo.jpg', 'rb'))

w = PostcardCreator(token)
w.send_free_card(postcard=card, mock_send=False)
