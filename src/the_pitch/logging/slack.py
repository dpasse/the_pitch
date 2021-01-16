import json
import sys
import requests


class Slack(object):

    def __init__(self, uri: str):
        self.uri = uri

    def write(self, message: str) -> None:
        payload = {
            'text': message,
        }

        try:
            requests.post(self.uri, json.dumps(payload))
        except:
            print("Unexpected error:", sys.exc_info()[0])

