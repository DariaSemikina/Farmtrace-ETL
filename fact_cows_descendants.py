import logging
from typing import List, Mapping, Optional

from google.cloud.bigquery import job

from config.settings import ProjectSettings, QuerySettings
from queries.cows_descendants import query_cows_descendants
from setup import bigquery_client

BIG_QUERY_CLIENT = bigquery_client()
BQ_SETTINGS = QuerySettings()
BQ_PROJECT_SETTINGS = ProjectSettings()

def query_job_config(
    settings: QuerySettings
) -> job.QueryJobConfig:
    """Retrieves the query job configuration."""
    return job.QueryJobConfig(
        allow_large_results=settings.allow_large_results,
        destination=settings.destination,
        use_legacy_sql=settings.use_legacy_sql,
        write_disposition=settings.write_disposition
    )


def insert_data_job(
    bq_settings: QuerySettings,
    bq_project_settings: ProjectSettings
) -> Optional[List[Mapping]]:
    """Inserts the query results into destination BQ table"""
    job_config = query_job_config(bq_settings)
    query = query_cows_descendants(bq_project_settings)
    query_job = BIG_QUERY_CLIENT.query(query, job_config)
    result = query_job.result()
    logging.info(f"The total number of rows: {result.total_rows}")
    return None


if __name__ == "__main__":
    insert_data_job(BQ_SETTINGS, BQ_PROJECT_SETTINGS)
