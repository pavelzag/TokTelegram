import logging
from mongoengine import *
from configuration import get_db_creds

# env = get_db_creds('ENV')
# test_uri = get_db_creds('test_uri')
# prod_uri = get_db_creds('prod_uri')
#
#
# if env == 'test':
#     client = MongoClient(test_uri)
#     db = client
# else:
#     client = MongoClient(prod_uri)
#     db = client
# print(db)

mongodb_db = get_db_creds(parameter_name='MONGODB_DB')
mongodb_uri = get_db_creds(parameter_name='MONGODB_URI')
mongodb_user = get_db_creds(parameter_name='MONGODB_USER')
mongodb_pass = get_db_creds(parameter_name='MONGODB_PASS')

logging.debug('This is the db: ' + mongodb_db + ' This is the uri: '
      + mongodb_uri + ' This is the user: ' + mongodb_user + ' This is the password: ' + mongodb_pass)

connect(mongodb_db, host=mongodb_uri, username=mongodb_user, password=mongodb_pass)


class Tok(Document):
    tok_id = StringField()
    tok_date = DateTimeField()


class Counter(Document):
    tok_tag = StringField()
    pass
