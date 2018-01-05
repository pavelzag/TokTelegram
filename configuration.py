from logger import logging_handler
import os.path
import yaml

if 'DYNO' in os.environ:
    is_heroku = True
else:
    is_heroku = False


def get_config(parameter_name):
    if is_heroku:
        logging_handler(os.environ.get(parameter_name))
        return os.environ.get(parameter_name, 'Theres\'s nothing here')
    else:
        with open("config.yml", 'r') as ymlfile:
            cfg = yaml.load(ymlfile)
            return cfg['creds'][parameter_name]


def get_db_creds(parameter_name):
    if is_heroku:
        logging_handler(os.environ.get(parameter_name))
        return os.environ.get(parameter_name, 'Theres\'s nothing here')
    else:
        with open("config.yml", 'r') as ymlfile:
            cfg = yaml.load(ymlfile)
            return cfg['db-params'][parameter_name]
