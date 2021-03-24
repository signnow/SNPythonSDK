from requests import post, put
from signnow_python_sdk.config import Config
from json import dumps,loads


class Template(object):

    @staticmethod
    def create(access_token, document_id, template_name=None):
        """Converts a document to a template and places it in the Templates folder

        Args:
            access_token (str): The access token for a user that has access to the document.
            document_id (str): The unique id of the document that will converted to a template.
            template_name (str): The name of the new template being created.

        Returns:
            dict: A dictionary representing the JSON response which includes the id of the new template or an error.
        """
        response = post(Config().get_base_url() + '/template', headers={
            "Authorization": "Bearer " + access_token,
            "Content-Type": "application/json",
            "Accept": "application/json"
        }, data=dumps({
            "document_id": document_id,
            "document_name": template_name
        }))

        return loads(response.content)

    @staticmethod
    def copy(access_token, template_id, document_name=None):
        """Creates a document copy from the provided template_id

        Args:
            access_token (str): The access token for a user that has access to the template.
            template_id (str): The unique id of the template you want to make a copy of.
            document_name (str): The name of the new document being created from the template.
        Returns:
            dict: A dictionary representing the JSON response which includes the unique id of the document created from
                the template
        """
        response = post(Config().get_base_url() + '/template/' + template_id + '/copy', headers={
            "Authorization": "Bearer " + access_token,
            "Content-Type": "application/json",
            "Accept": "application/json"
        }, data=dumps({
            "document_name": document_name
        }))

        return loads(response.content)

    @staticmethod
    def update(access_token, template_id, data_payload):
        """Update a document with fields, texts, and check marks.

        Args:
            access_token (str): The access token for the user account that has access to the document.
            document_id (str): The unique id of the document you want to update.
            data_payload (dict): A dictionary representing the data payload passed in the request body. See the
                API documention on how to consstruct it https://campus.barracuda.com/product/signnow/article/CudaSign/RestEndpointsAPI/

        Returns:
            dict: The JSON response from the API which includes the document id and arrays of elements added to the
                document
        """
        response = put(Config().get_base_url() + '/document/' + template_id, headers={
            "Authorization": "Bearer " + access_token,
            "Content-Type": "application/json",
            "Accept": "application/json"
        }, data=dumps(data_payload))

        return loads(response.content)

    @staticmethod
    def invite(access_token, template_id, invite_payload):
        """Send an invite for a document via the API

        Args:
            access_token (str): The access token for the user account that has access to the document.
            template_id (str): The unique id of the document you want to send an invite for.
            invite_payload (dict): A dictionary representing the invite payload for sending an invite.

        Returns:
            dict: The JSON response from the API {u'result': u'success'} or JSON representing an API error.
        """
        response = post(Config().get_base_url() + '/document/' + template_id + '/invite', headers={
            "Authorization": "Bearer " + access_token,
            "Accept": "application/json",
            "Content-Type": "application/json"
        }, data=dumps(invite_payload))

        return loads(response.content)


    @staticmethod
    def routing_detail(access_token, template_id, template_routing_payload):
        """Creates a document copy from the provided template_id

        Args:
            access_token (str): The access token for a user that has access to the template.
            template_id (str): The unique id of the template you want to make a copy of.
            document_name (str): The name of the new document being created from the template.
        Returns:
            dict: A dictionary representing the JSON response which includes the unique id of the document created from
                the template
        """
        response = post(Config().get_base_url() + '/document/' + template_id+ '/template/routing/detail', headers={
            "Authorization": "Bearer " + access_token,
            "Content-Type": "application/json",
            "Accept": "application/json"
        }, data = dumps(template_routing_payload))

        return loads(response.content)

