import json
import requests
import time
from configuration import get_config
from query_builder import save_query, get_random_tok

TOKEN = get_config('TOKEN')
white_list = get_config('WHITE_LIST')
URL = "https://api.telegram.org/bot{}/".format(TOKEN)
telegram_success_msg = 'Message was received succesfully.'
telegram_failure_msg = 'Message was not received succesfully.'


def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def post_url(url):
    response = requests.post(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates(offset=None):
    url = URL + "getUpdates?timeout=100"
    if offset:
        url += "&offset={}".format(offset)
    js = get_json_from_url(url)
    return js


def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)


def get_last_chat_id_and_text(updates, text=False):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    if not text:
        voice_id = updates['result'][last_update]['message']['voice']['file_id']
        return chat_id, voice_id
    else:
        return chat_id


def send_message(text, chat_id):
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)


def send_voice(voice_id, chat_id):
    url = URL + "sendVoice?voice={}&chat_id={}".format(voice_id, chat_id)
    post_url(url)


def is_voice(updates):
    try:
        num_updates = len(updates["result"])
        last_update = num_updates - 1
        voice_id = updates['result'][last_update]['message']['voice']['file_id']
        return True
    except:
        return False


def main():
    last_update_id = None
    while True:
        updates = get_updates(last_update_id)
        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1
            if is_voice(updates):
                chat_id, voice_id = get_last_chat_id_and_text(updates)
                save_query(voice_id)
                send_message('Tok saved', chat_id)
            else:
                chat_id = get_last_chat_id_and_text(updates, text=True)
                voice_id = get_random_tok()
                send_voice(voice_id, chat_id)
        time.sleep(0.5)


if __name__ == '__main__':
    main()
