import logging
import azure.functions as func
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from shared_code import azure_config
import json

environment_vars = azure_config()

# Set Azure Search endpoint and key
endpoint = f'https://{environment_vars["search_service_name"]}.search.windows.net'
key = environment_vars["search_api_key"]

# Your index name
index_name = 'good-books'

# Create Azure SDK client
search_client = SearchClient(endpoint, index_name, AzureKeyCredential(key))

def main(req: func.HttpRequest) -> func.HttpResponse:

    if docid := req.params.get('id'):
        logging.info(f"/Lookup id = {docid}")
        returnedDocument = search_client.get_document(key=docid)

        full_response = {"document": returnedDocument}
        return func.HttpResponse(body=json.dumps(full_response), mimetype="application/json", status_code=200)
    else:
        return func.HttpResponse(
             "No doc id param found.",
             status_code=200
        )
