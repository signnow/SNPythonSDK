from base64 import b64encode
import unirest

CLIENT_ID = ''
CLIENT_SECRET = ''
BASE_URL = ''

class Config(object):

    def __init__(self, options=None, **kwargs):
        global CLIENT_ID, CLIENT_SECRET, BASE_URL
        dicts = [options or {}, kwargs]

        for d in dicts:
            for k, v in d.iteritems():
                kwargs.setdefault(k, v)

        if len(kwargs):
            for k, v in kwargs.iteritems():
                setattr(self, k, v)

            if 'client_id' in kwargs:
                CLIENT_ID = kwargs['client_id']
            if 'client_secret' in kwargs:
                CLIENT_SECRET = kwargs['client_secret']
            if 'base_url' in kwargs:
                BASE_URL = kwargs['base_url']
            if 'timeout' in kwargs:
                unirest.timeout(kwargs['timeout'])
        else:
            self.client_id = CLIENT_ID
            self.client_secret = CLIENT_SECRET
            self.base_url = BASE_URL

    def get_client_id(self):
        return self.client_id

    def get_client_secret(self):
        return self.client_secret

    def get_base_url(self):
        return self.base_url

    def get_encoded_credentials(self):
        return b64encode(self.client_id + ':' + self.client_secret)
