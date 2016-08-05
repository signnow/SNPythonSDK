from unirest import post
from config import Config
from json import dumps


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
        }, params=dumps({
            "document_id": document_id,
            "document_name": template_name
        }))

        return response.body

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
        }, params=dumps({
            "document_name": document_name
        }))

        return response.body
