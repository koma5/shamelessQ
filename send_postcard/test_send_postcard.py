from postcard_creator.postcard_creator import PostcardCreator, Postcard, Token, Recipient, Sender

token = Token()
token.fetch_token(username='', password='')
token.has_valid_credentials(username='marco@5th.ch', password='ythTt96rjEzuWqD')
recipient = Recipient(prename='Marco', lastname='Koch', street='Niederwies 18', place='Vorderthal', zip_code=8857)
sender = Sender(prename='Marco', lastname='Koch', street='Niederwies 18', place='Vorderthal', zip_code=8857)
card = Postcard(message='test', recipient=recipient, sender=sender, picture_stream=open('./my-photo.jpg', 'rb'))

w = PostcardCreator(token)
w.send_free_card(postcard=card, mock_send=False)
