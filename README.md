# farmtrace-assignment
* extract Big Query source cows table 
* calls SQL query that transforms the source table (2) according to the business logic 
* loads the results (with overwrite rule) into BigQuery destination data mart ()

## Business Requirements

* We need an ANSI SQL statement that will return all the cows together with all their lineal – direct
descendants, showing also the depth of the relation (1-child, 2-grandchild etc.) Cows with no
descendants will not be included in the result set. (DONE)
* The result set of the step (a) needs to be saved in our data lake. We need to use Python to do so.
You can use the file format of your choice. (TBD)
* The file that has been created in step (b) will be the source of an ETL/ELT process that populates
one of our data marts, implemented on a relational db. The target table has the same structure as
the file in the data lake and previous data can be overwritten. (DONE)

Please take into account the solution was implemented using Google BigQuery as an alternative of Azure Redshift.
There is still a room for improvement in different aspects: 1. unit tests (pytest could be used for that) 2. the source/destination tables could be extended to have date field and partitioning. It could increase the speed for reading the data from cows table and the destination table could be also loaded incrementally. 3. job orchestration and scheduler (Apache Airflow, Airbyte, Azure Databricks, etc.)
works nicely with different services and 4. containerization using Docker

## To run the application:

```bash
python etl_job.py
```
