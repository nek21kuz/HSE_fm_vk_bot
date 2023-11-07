import content, json

def get_but(text, color):
    return {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"" + "1" + "\"}",
                    "label": f"{text}"
                },
                "color": f"{color}"
            }

lst_spliter = lambda lst, sz: [lst[i:i+sz] for i in range(0, len(lst), sz)]

keyboard_void = {
    "one_time" : True,
    "buttons" : []
}

keyboard_main = {
    "one_time" : False,
    "buttons" : [
        [get_but('Музыка', 'positive'), get_but('Подкасты', 'positive')],
        [get_but('Предсказание', 'positive'), get_but('Мяу', 'positive')]
    ]
}
keyboard_main = json.dumps(keyboard_main, ensure_ascii = False).encode('utf-8')
keyboard_main = str(keyboard_main.decode('utf-8'))

keyboard_music = {
    "one_time" : False,
    "buttons" : lst_spliter([get_but(i.capitalize(), 'positive') for i in content.pl_music],2) +\
    [[get_but('Назад', 'negative')]]
}

keyboard_music = json.dumps(keyboard_music, ensure_ascii = False).encode('utf-8')
keyboard_music = str(keyboard_music.decode('utf-8'))

keyboard_podcast = {
    "one_time" : False,
    "buttons" : lst_spliter([get_but(i.capitalize(), 'positive') for i in content.pl_pc],2) +\
    [[get_but('Назад', 'negative')]]
}
keyboard_podcast = json.dumps(keyboard_podcast, ensure_ascii = False).encode('utf-8')
keyboard_podcast = str(keyboard_podcast.decode('utf-8'))
