SignNow
=======

SignNow Python SDK

About SignNow
-------------

SignNow is a powerful web-based e-signature solution that streamlines the signing process and overall document flow for businesses of any size. SignNow offers SaaS as well as public and private cloud deployment options using the same underlying API. With SignNow you can easily sign, share and manage documents in compliance with international data laws and industry-specific regulations. SignNow enables you to collect signatures from partners, employees and customers from any device within minutes. 

API Contact Information
-----------------------

If you have questions about the SignNow API, please visit [https://help.signnow.com/docs](https://help.signnow.com/docs) or email [api@signnow.com](mailto:api@signnow.com).

See additional contact information at the bottom.

Installation
============

To install to Python library:

::

    pip install signnow-python-sdk 

Or clone the SignNow library and extract it into the location of your
choice.

Navigate to the extracted file and run the following:

::

    python setup.py install

Setup
=====

.. code:: python

    import signnow_python_sdk

    signnow_python_sdk.Config(client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", environment="production")
    
    Environments: 
          production - https://api.signnow.com
          eval - https://api-eval.signnow.com

Examples
========

To run the examples you will need an API key. You can get one here [https://www.signnow.com/api](https://www.signnow.com/api). For a full list of accepted parameters, refer to the SignNow REST Endpoints API guide: [https://help.signnow.com/docs](https://help.signnow.com/docs).

OAuth2
======

Request OAuth Token
-------------------

.. code:: python

    access_token = signnow_python_sdk.OAuth2.request_token("YOUR USERNAME", "YOUR PASSWORD")

Verify OAuth Token
------------------

.. code:: python

    access_token_verify = signnow_python_sdk.OAuth2.verify(AccessToken)

User
====

Create New User
---------------

.. code:: python

    new_user = signnow_python_sdk.User.create("name@domain.com", "newpassword", "Firstname", "Lastname")

Retreive User Account Information
---------------------------------

.. code:: python

    sn_user = signnow_python_sdk.User.get(access_token)

Document
========

Get Document
------------

.. code:: python

    # without annotations
    document_data = signnow_python_sdk.Document.get(access_token, "YOUR_DOCUMENT_ID")

    # with annotations
    document_data = signnow_python_sdk.Document.get(access_token, "YOUR_DOCUMENT_ID", True)

Create New Document
-------------------

.. code:: python

    dir_path = os.path.dirname(os.path.realpath(__file__)) + '/testing123.pdf'
    doc_id = signnow_python_sdk.Document.upload(access_token, dir_path, False)

Create New Document and Extract the Fields
------------------------------------------

.. code:: python

    dir_path = os.path.dirname(os.path.realpath(__file__)) + '/testing123.pdf'
    doc_id = signnow_python_sdk.Document.upload(access_token, dir_path)

Update Document
---------------

.. code:: python

    update_payload = {
        "texts": [
            {
                "size": 22,
                "x": 61,
                "y": 72,
                "page_number": 0,
                "font": "Arial",
                "data": "a sample text element",
                "line_height": 9.075,
                "client_timestamp": datetime.now().strftime("%s")
            }
        ],
        fields: [
            {
                "x": 10,
                "y: 10,
                "width": 122,
                "height": 34,
                "page_number": 0,
                "role": "Buyer",
                "required": True,
                "type": "signature"
            }
        ]
    }

    update_doc_res = signnow_python_sdk.Document.update(access_token, doc_id, update_payload)

Delete Document
---------------

.. code:: python

    delete_doc_res = signnow_python_sdk.Document.delete(access_token, doc_id)

Download Document
-----------------

.. code:: python

    # without history
    download_doc_res = signnow_python_sdk.Document.download(access_token, "YOUR DOCUMENT ID", "/", "sample")

    # with history
    download_doc_res = signnow_python_sdk.Document.download(access_token, "YOUR DOCUMENT ID", "/", "sample", True)

Send Free Form Invite
---------------------

.. code:: python

    invite_payload = new
    {
      "from": "account_email@domain.com",
      "to": "name@domain.com"
    }

    freeform_invite_res = signnow_python_sdk.Document.invite(access_token, "YOUR DOCUMENT ID", invite_payload)

Send Role-based Invite
----------------------

.. code:: python

    invite_payload = {
      "to": [
        {
          "email": "name@domain.com",
          "role_id": "",
          "role": "Role 1",
          "order": 1,
          "authentication_type": "password",
          "password": "SOME PASSWORD",
          "expiration_days": 15,
          "reminder": 5
        },
        {
          "email": "name@domain.com",
          "role_id": "",
          "role": "Role 2",
          "order": 2,
          "authentication_type": "password",
          "password": "SOME PASSWORD",
          "expiration_days": 30,
          "reminder": 10
        }
      ],
      "from": "your_account_email@domain.com",
      "cc": [
        "name@domain.com"
      ],
      "subject": "YOUR SUBJECT",
      "message": "YOUR MESSAGE"
    };

    role_based_invite_res = signnow_python_sdk.Document.invite(access_token, "YOUR DOCUMENT ID", invite_payload)

Cancel Invite
-------------

.. code:: python

    cancel_invite_res = signnow_python_sdk.Document.cancel_invite(access_token, "YOUR DOCUMENT ID");

Merge Existing Documents
------------------------

.. code:: python

    merge_doc_payload = {
      "name": "My New Merged Doc",
      "document_ids": ["YOUR DOCUMENT ID", "YOUR DOCUMENT ID"]
    }

    merge_doc_res = signnow_python_sdk.Document.merge_and_download(access_token, mergeDocsObj, "/", "sample-merge");

Document History
----------------

.. code:: python

    doc_history_res = signnow_python_sdk.Document.get_history(access_token, "YOUR DOCUMENT ID");

Template
========

Create Template
---------------

.. code:: python

    new_template_res = signnow_python_sdk.Template.create(access_token, "YOUR DOCUMENT ID", "My New Template");

Copy Template
-------------

.. code:: python

    copy_template_res = signnow_python_sdk.Template.copy(access_token, "YOUR TEMPLATE ID", "My Copy Template Doc");

Folder
======

+------------------------+-----------------------------------------------------------------------+
| Filters                | Values                                                                |
+========================+=======================================================================+
| ``signing-status``     | ``waiting-for-me``, ``waiting-for-others``, ``signed``, ``pending``   |
+------------------------+-----------------------------------------------------------------------+
| ``document-updated``   | ``datetime.now().strftime("%s")``                                     |
+------------------------+-----------------------------------------------------------------------+
| ``document-created``   | ``datetime.now().strftime("%s")``                                     |
+------------------------+-----------------------------------------------------------------------+

+---------------------+--------------------+
| Sort                | Values             |
+=====================+====================+
| ``document-name``   | ``asc``/``desc``   |
+---------------------+--------------------+
| ``updated``         | ``asc``/``desc``   |
+---------------------+--------------------+
| ``created``         | ``asc``/``desc``   |
+---------------------+--------------------+

Get users root folder
---------------------

.. code:: python

    root_folder_Res = signnow_python_sdk.Folder.root_folder(access_token);

Get Folder
----------

.. code:: python

    get_folder_res = signnow_python_sdk.Folder.get(access_token, "YOUR FOLDER ID");

Webhook
=======

Create Webhook
--------------

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Events                | Description                                                                                                 |
+=======================+=============================================================================================================+
| ``document.create``   | Webhook is triggered when a document is uploaded to users account in SignNow                                |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| ``document.update``   | Webhook is triggered when a document is updated (fields added, text added, signature added, etc.)           |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| ``document.delete``   | Webhook is triggered when a document is deleted from                                                        |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| ``invite.create``     | Webhook is triggered when an invitation to a SignNow document is created.                                   |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| ``invite.update``     | Webhook is triggered when an invite to Signnow document is updated. Ex. A signer has signed the document.   |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

.. code:: python

    createWebhookRes = signnow_python_sdk.Webhook.create(access_token, "document.create", "YOUR URL");

List Webhooks
-------------

.. code:: python

    list_webhooks_res = signnow_python_sdk.Webhook.list_all(access_token);

Delete Webhook
--------------

.. code:: python

    delete_webhook_res = signnow_python_sdk.Webhook.delete(AccessToken, "YOUR WEBHOOK ID");

Link
====

Create Link
-----------

.. code:: python

    create_link_res = signnow_python_sdk.Link.create(access_token, "YOUR DOCUMENT ID");

LICENSE
-------

This project is released under the Apache 2.0 [License](https://github.com/signnow/SNPythonSDK/blob/master/LICENSE.md).

Additional Contact Information
==============================

SUPPORT
-------

To contact SignNow support, please email [support@signnow.com](mailto:support@signnow.com).

SALES
-----

For pricing information please call (800) 831-2050 or email [sales@signnow.com](mailto:sales@signnow.com).
