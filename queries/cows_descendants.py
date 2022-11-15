

from config.settings import ProjectSettings


def query_cows_descendants(
    settings: ProjectSettings
) -> str:
    query = f""" WITH RECURSIVE COWS_DESCENDANTS_CTE AS
    (
    SELECT
        CowUNID,
        CowUNID_Father,
        CowUNID_Mother,
        CowUNID AS Descendants,
        0 AS Depth
    FROM `{settings.project_id}`.`{settings.dataset}`.`{settings.table}`
        CowUNID_Father IS NULL
        AND CowUNID_Mother IS NULL
    UNION ALL
    SELECT
        c.CowUNID,
        c.CowUNID_Father,
        c.CowUNID_Mother,
        CONCAT(Descendants, ',', c.CowUNID) AS Descendants,
        Depth + 1
        FROM `{settings.project_id}`.`{settings.dataset}`.`{settings.table}` c
        INNER JOIN COWS_DESCENDANTS_CTE cdc ON
        cdc.CowUNID = c.CowUNID_Father  OR  cdc.CowUNID = c.CowUNID_Mother
    )
    SELECT
        SPLIT(Descendants, ',')[OFFSET(0)] AS CowUNID,
        REPLACE(
            Descendants,
            CONCAT(SPLIT(Descendants, ',')[OFFSET(0)], ','), "") AS Descendants,
        Depth
    FROM COWS_DESCENDANTS_CTE
    WHERE
        CowUNID_Father IS NOT NULL
        AND CowUNID_Mother IS NOT NULL
    ORDER BY
        Depth,
        CowUNID
    """
    return query
