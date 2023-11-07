import keyboards, connect


def send(id, text):
    connect.vk.messages.send(user_id = id, message = text, random_id = 0)

def send_sticker(id, number):
    connect.vk.messages.send(user_id = id, sticker_id = number, random_id = 0)

def send_attachment(id, url):
    connect.vk.messages.send(user_id = id, attachment = url, random_id = 0)

def send_void_kb(id, text):
    connect.vk_session.method('messages.send', \
                      {'user_id' : id, 'message' : text,\
                       'random_id' : 0, 'keyboard' : keyboards.keyboard_void})

def send_main_kb(id, text):
    connect.vk_session.method('messages.send', \
                      {'user_id' : id, 'message' : text,\
                       'random_id' : 0, 'keyboard' : keyboards.keyboard_main})
    
def send_music_kb(id, text):
    connect.vk_session.method('messages.send', \
                      {'user_id' : id, 'message' : text,\
                       'random_id' : 0, 'keyboard' : keyboards.keyboard_music})
    
def send_podcast_kb(id, text):
    connect.vk_session.method('messages.send', \
                      {'user_id' : id, 'message' : text,\
                       'random_id' : 0, 'keyboard' : keyboards.keyboard_podcast})
