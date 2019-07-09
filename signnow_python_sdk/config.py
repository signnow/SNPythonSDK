from base64 import b64encode

CLIENT_ID = ''
CLIENT_SECRET = ''
BASE_URL = ''
PRODUCTION_BASE_URL = 'https://api.signnow.com'
EVAL_BASE_URL = 'https://eval.signnow.com'


class Config(object):

    def __init__(self, options=None, **kwargs):
        global CLIENT_ID, CLIENT_SECRET, BASE_URL
        dicts = [options or {}, kwargs]

        for d in dicts:
            for k, v in d.items():
                kwargs.setdefault(k, v)

        if len(kwargs):
            for k, v in kwargs.items():
                setattr(self, k, v)

            if 'client_id' in kwargs:
                CLIENT_ID = kwargs['client_id']
            if 'client_secret' in kwargs:
                CLIENT_SECRET = kwargs['client_secret']
            if 'environment' in kwargs:
                if kwargs['environment'] == 'production':
                    BASE_URL = PRODUCTION_BASE_URL
                else:
                    BASE_URL = EVAL_BASE_URL
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
        return b64encode((self.client_id + ':' + self.client_secret).encode('utf-8')).decode('utf-8')
