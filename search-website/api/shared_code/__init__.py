import os

def azure_config():

    configs = {
        "search_facets": "authors*,language_code",
        "search_index_name": os.environ.get("SearchIndexName", ""),
    }

    configs["search_service_name"]=os.environ.get("SearchServiceName","")
    configs["search_api_key"]=os.environ.get("SearchApiKey","")

    return configs
