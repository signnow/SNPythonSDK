from requests import get, post, put, delete
from signnow_python_sdk.config import Config
from datetime import datetime
import os
from json import dumps, loads


class Document(object):

    @staticmethod
    def get(access_token, document_id, with_annotation=False):
        """Request a document from the Signnow API  by document id using unirest

        Args:
            access_token (str): The access token for a user that has access to the document.
            document_id (str): The unique id of the document you want to retrieve for the API.
            with_annotation (bool): A boolean indicating whether or not to return integration objects.

        Returns:
            dict: The JSON response from the API which includes the attributes of the document
                or the error returned.
        """
        response = get(Config().get_base_url() + '/document/' + document_id + ('?with_annotation=true' if with_annotation else ''), headers={
            "Authorization": "Bearer " + access_token,
            "Accept": "application/json"
        })

        return loads(response.content)

    @staticmethod
    def upload(access_token, file_path, field_extract=True):
        """Request a document from the Signnow API  by document id using unirest

        Args:
            access_token (str): The access token for a user account you want to upload the document to.
            file_path (str): The file path to the document you want to upload to signnow.
            field_extract (bool): A boolean indicating whether or not to extract field tags in the document.

        Returns:
            dict: The JSON response from the API which includes the id of the document uploaded.
                or the error returned.
        """
       # timeout(60)
        print(file_path)
        #file = {'file': open(file_path, mode="rb", encoding="ISO-8859-1")}
        file = {'file': open(file_path, mode="rb")}
        response = post(Config().get_base_url() + '/document' , headers={
            "Authorization": "Bearer " + access_token
        }, data={
         #  "file": file,
            "client_timestamp": datetime.now().strftime("%s"),
            "check_fields": field_extract
        }, files = file
        )

        return loads(response.content)

    @staticmethod
    def update(access_token, document_id, data_payload):
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
        response = put(Config().get_base_url() + '/document/' + document_id, headers={
            "Authorization": "Bearer " + access_token,
            "Content-Type": "application/json",
            "Accept": "application/json"
        }, data=dumps(data_payload))

        return loads(response.content)

    @staticmethod
    def download(access_token, document_id, file_name='my-collapsed-document', file_path='', with_history=False):
        """Download a document from a signnow account and save it to a specified file path and file name

        Args:
            access_token (str): The access token for the user account that has access to the document.
            document_id (str): The unique id of the document you want to download.
            file_name (str): The name of the file that will be created and written to.
            file_path (str): The file path where the newly download file will be created.
            with_history (bool): A boolean indicating whether or not to download the doucment history with the document.

        Returns:
            str or dict: The byte string of the document's raw data being returned by the API. If there is an error it
                will return a dictionary with error data.
        """
        response = get(Config().get_base_url() + '/document/' + document_id + '/download/collapsed' + ('?with_history=1' if with_history else ''), headers={
            "Authorization": "Bearer " + access_token
        })

        if file_path != '':
            path = os.path.abspath(file_path) + '/' + file_name + '.pdf'
        else:
            path = os.getcwd() + '/' + file_name + '.pdf'

        if not os.path.isfile(path):
            new_file = open(path, 'wb+')
            new_file.write(response.content)
            new_file.close()
        else:
            file_path, full_file_name = os.path.split(path)
            file_name, file_extension = os.path.splitext(full_file_name)
            i = 1
            while os.path.exists(file_path + '/' + file_name + '(%s).pdf' % i):
                i += 1
            new_file = open(file_path + '/' + file_name + '(%s).pdf' % i, 'wb+')
            new_file.write(response.content)
            new_file.close()

        return response.content

    @staticmethod
    def delete(access_token, document_id):
        """Delete a document that has been uploaded to a users account

        Args:
            access_token (str): The access token for the user account that has access to the document.
            document_id (str): The unique id of the document you want to delete.

        Returns:
            dict: The JSON response from the API {u'result': u'success'} or JSON representing an API error.
        """
        response = delete(Config().get_base_url() + '/document/' + document_id, headers={
            "Authorization": "Bearer " + access_token,
            "Accept": "application/json"
        })

        return loads(response.content)

    @staticmethod
    def invite(access_token, document_id, invite_payload):
        """Send an invite for a document via the API

        Args:
            access_token (str): The access token for the user account that has access to the document.
            document_id (str): The unique id of the document you want to send an invite for.
            invite_payload (dict): A dictionary representing the invite payload for sending an invite.

        Returns:
            dict: The JSON response from the API {u'result': u'success'} or JSON representing an API error.
        """
        response =  post(Config().get_base_url() + '/document/' + document_id + '/invite', headers={
            "Authorization": "Bearer " + access_token,
            "Accept": "application/json",
            "Content-Type": "application/json"
        }, data=dumps(invite_payload))

        return loads(response.content)

    @staticmethod
    def cancel_invite(access_token, document_id):
        """Cancel all invites on a document.

        Args:
            access_token (str): The access token for the user account that has access to the document.
            document_id (str): The unique id of the document you want to cancel all invites for.

        Returns:
            dict: The JSON response from the API {u'result': u'success'} or JSON representing an API error.
        """
        response = put(Config().get_base_url() + '/document/' + document_id + '/fieldinvitecancel', headers={
            "Authorization": "Bearer " + access_token,
            "Accept": "application/json",
        })

        return loads(response.content)

    @staticmethod
    def download_link(access_token, document_id):
        """Creates a link that when opened in a browser will allow you to download the document one time.

        Args:
            access_token (str): The access token for the user account that has access to the document.
            document_id (str): The unique id of the document you want to create the link for.

        Returns:
            dict: The JSON response from the API with the download link or JSON representing an API error.
        """
        response = post(Config().get_base_url() + '/document/' + document_id + '/download/link', headers={
            "Authorization": "Bearer " + access_token,
            "Accept": "application/json",
            "Content-Type": "application/json"
        })

        return loads(response.content)

    @staticmethod
    def merge_and_download(access_token, document_ids, file_name='my-merged-document', file_path=''):
        """Merges two or more documents and then saves the response to a specified file name and file path

        Args:
            access_token (str): The access token for the user account that has access to the document.
            document_ids (list): A list of document unique ids that will be merged.
            file_name (str): The name of the file that will be created and written to.
            file_path (str): The file path where the newly download file will be created.

        Returns:
            str or dict: The byte string of the merged document's raw data being returned by the API. If there is an
            error it will return a dictionary with error data.
        """
        print (type(document_ids))
        response = post(Config().get_base_url() + '/document/merge', headers={
            "Authorization": "Bearer " + access_token,
            "Content-Type": "application/json"
        }, data=dumps({
            "name": file_name,
            "document_ids": document_ids
        }))

        if file_path != '':
            path = os.path.abspath(file_path) + '/' + file_name + '.pdf'
        else:
            path = os.getcwd() + '/' + file_name + '.pdf'

        if not os.path.isfile(path):
            new_file = open(path, 'wb+')
            new_file.write(response.content)
            new_file.close()
        else:
            file_path, full_file_name = os.path.split(path)
            file_name, file_extension = os.path.splitext(full_file_name)
            i = 1
            while os.path.exists(file_path + '/' + file_name + '(%s).pdf' % i):
                i += 1
            new_file = open(file_path + '/' + file_name + '(%s).pdf' % i, 'wb+')
            new_file.write(response.content)
            new_file.close()

        return response.content

    @staticmethod
    def get_history(access_token, document_id):
        """Creates a link that when opened in a browser will allow you to download the document one time.

        Args:
            access_token (str): The access token for the user account that has access to the document.
            document_id (str): The unique id of the document you want to get the history of.

        Returns:
            list: A list of document history events or JSON representing an API error.
        """
        response = get(Config().get_base_url() + '/document/' + document_id + '/historyfull', headers={
            "Authorization": "Bearer " + access_token,
            "Accept": "application/json"
        })

        return loads(response.content)

    @staticmethod
    def move(access_token, document_id, folder_id):
        """Cancel all invites on a document.

        Args:
            access_token (str): The access token for the user account that has access to the document.
            document_id (str): The unique id of the document you want to move.
            folder_id (str): The unique id of the folder you want to move the document to.

        Returns:
            dict: The JSON response from the API {u'result': u'success'} or JSON representing an API error.
        """
        response = post(Config().get_base_url() + '/document/' + document_id + '/move', headers={
            "Authorization": "Bearer " + access_token,
            "Accept": "application/json",
            "Content-Type": "application/json"
        }, data=dumps({
            "folder_id": folder_id
        }))

        return loads(response.content)
