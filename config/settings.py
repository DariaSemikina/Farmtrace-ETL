from pydantic import BaseSettings


class QuerySettings(BaseSettings):
    allow_large_results: bool = True
    destination: str = "funda-bi-dev.dbt_darya_adhoc.cows_descendants"
    use_legacy_sql: bool = False
    write_disposition: str = "WRITE_TRUNCATE"

class ProjectSettings(BaseSettings):
    project_id: str = "test-project"
    dataset: str = "test-dataset"
    table: str = "cows-table"
