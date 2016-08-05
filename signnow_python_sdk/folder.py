from unirest import get
from config import Config


class Folder(object):

    @staticmethod
    def root_folder(access_token):
        """Return information about a users root folder including an array of all their folders like \"Documents\",
            \"Templates\", etc.

        Args:
            access_token (str): An access token belonging to the user you want to retrieve the root folder for.

        Returns:
            dict: A dictionary representing the JSON data of the root folder or the error returned by the API
        """
        response = get(Config().get_base_url() + '/folder', headers={
            "Authorization": "Bearer " + access_token,
            "Accept": "application/json"
        })

        return response.body

    @staticmethod
    def get(access_token, folder_id, number_of_documents=20, offset=0, filter_object={}, sort_object={}):
        """Return the JSON data of a folder including its subfolders, documents and other data.

        Args:
            access_token (str): An access token belonging to the user you want to retrieve the folder for.
            folder_id (str): The unique id of the folder you want to retrieve.
            number_of_documents (int): The number of documents you want to retrieve with a max of 100
            offset (int): The offset from the beging of the documents list. Used for paging.
            filter_object (dict): A dictionary to pass filter settings for the folder.
            sort_object (dict): A dictionary to pass sorting options to the API

        Returns:
            dict: A dictionary representing the JSON data of the folder or the error returned by the API
        """
        if number_of_documents > 100:
            number_of_documents = 100

        folder_url = Config().get_base_url() + '/folder/' + folder_id + '/?offset=' + str(offset) + '&limit=' + \
                     str(number_of_documents)

        if 'filters' in filter_object and 'filter-values' in filter_object:
            folder_url = folder_url + '&filters=' + filter_object['filters'] + '&filter-values=' + filter_object['filter-values']

        if 'sortby' in sort_object and 'order' in sort_object:
            folder_url = folder_url + '&sortby=' + sort_object['sortby'] + '&order=' + sort_object['order']

        response = get(folder_url, headers= {
            "Authorization": "Bearer " + access_token,
            "Accept": "application/json"
        })

        return response.body
