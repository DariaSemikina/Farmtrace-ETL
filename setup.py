from google.cloud import bigquery
from google.oauth2 import service_account

from etl_job import BQ_PROJECT_SETTINGS

PROJECT_ID = BQ_PROJECT_SETTINGS.project_id
PATH_TO_KEYS = "keys/bigquery/BQ_keys.json"


def set_bigquery_credentials():
    """Sets up Big Query credentials for the context"""
    return service_account.Credentials.from_service_account_file(PATH_TO_KEYS)


def bigquery_client() -> bigquery.Client:
    """Initializes the BigQuery Client."""
    bq_credentials = set_bigquery_credentials()
    return bigquery.Client(credentials=bq_credentials, project=PROJECT_ID)
