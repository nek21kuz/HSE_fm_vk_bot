import vk_api
from tok import main_token
from vk_api.longpoll import VkLongPoll, VkEventType

def connect():
    global vk, longpoll, vk_session
    vk_session = vk_api.VkApi(token = main_token)
    vk = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
   
