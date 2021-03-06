from dbconnector import Tok
from random import randrange
from datetime import datetime
import uuid
import exceptions

date = datetime.now()
tok_id = str(uuid.uuid4())


def save_query(voice_id):
    tok_obj = Tok(tok_date=date, tok_id=voice_id)
    try:
        tok_obj.save()
    except:
        raise exceptions.SaveToDBException


def tok_counter():
    num_objects = Tok.objects.count()
    Tok.objects[randrange(0, num_objects-1)]
    print(num_objects)


def get_random_tok():
    num_objects = Tok.objects.count()
    random_obj_number = randrange(0, num_objects-1)
    random_tok_obj = Tok.objects[random_obj_number]
    return random_tok_obj.tok_id