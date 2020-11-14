import telepot

def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'text':
        name = msg["from"]["first_name"]
        txt = msg['text']
        bot.sendMessage(chat_id, 'Hello %s, I am a stupid bot!'%name)
        bot.sendMessage(chat_id, 'I have received this: %s'%txt)

TOKEN = 'insert_your_token'

bot = telepot.Bot(TOKEN)
bot.message_loop(on_chat_message)

print('Listening ...')

import time
while 1:
    time.sleep(10)
