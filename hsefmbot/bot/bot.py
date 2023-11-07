import random
import content, messages, connect


def interface():

    for event in connect.longpoll.listen():    
        if event.type == connect.VkEventType.MESSAGE_NEW and event.to_me:

            msg = event.text.lower()
            id = event.user_id


                        #dialogs

            
            if msg == 'начать' or msg == 'start':
                name = connect.vk.users.get(user_ids = id)[0]['first_name']
                messages.send_main_kb(id, 'Приветики, ' + name + '! Я бот HSE FM\n' +
                            'Можешь послушать музыку, подкасты')
                
            elif msg == 'назад':
                messages.send_main_kb(id, 'Чего ещё хочешь?м?')

            elif msg == 'связь с администратором':
                messages.send_void_kb(id, 'Скоро с вами свяжуться')
                messages.send_main_kb(492471937, 'booy')



            elif msg == 'музыка':
                messages.send_music_kb(id, 'Итак, из музыки у нас сегодня:\n'+
                              ', '.join(content.pl_music))
            elif msg in content.pl_music:
                    messages.send_attachment(id, \
                                    content.data_music[msg]\
                                    [random.randint(0, len(content.data_music[msg]) - 1)])

                    

            elif msg == 'подкасты':
                messages.send_podcast_kb(id, 'Итак, из подкастов у нас сегодня:\n'+
                              ', '.join(content.pl_pc))
            elif msg in content.pl_pc:
                    messages.send_attachment(id, \
                                    content.data_pc[msg]\
                                    [random.randint(0, len(content.data_pc[msg]) - 1)])



            elif msg in content.pl_predict:
                    messages.send_attachment(id, \
                                    content.data_predict[msg]\
                                    [random.randint(0, len(content.data_predict[msg]) - 1)])



            else:
                messages.send(id, 'не понимаю :)')


while True:
    try:
        connect.connect()
        interface()
    except:
        messages.send(492471937, 'blia')
