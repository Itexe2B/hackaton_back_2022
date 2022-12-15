import pandas as pd
import json
class Session:
    __instance = None
    session = None
    @staticmethod
    def get_instance():
        if Session.__instance is None :
            Session.__instance = Session()
        return Session.__instance

    def __init__(self):
        with open('session.json') as json_file:
            Session.session = json.load(json_file)

    def put_session(self, key, value):
        Session.session[key] = value
        with open('session.json', 'w') as outfile:
            json.dump(Session.session, outfile)