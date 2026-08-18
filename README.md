# JobAPI_Databricks

This is an end-to-end data engineering project that was developed using Databricks.

# Sample Architecture

<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/0c3960aa-4361-495e-91c4-e750cff15917" />

# Data Lineage

<img width="1776" height="1072" alt="image" src="https://github.com/user-attachments/assets/1498d5b5-b013-4741-92c2-eb510ad3698e" />

# Job Scheduler

<img width="1416" height="574" alt="image" src="https://github.com/user-attachments/assets/87678fe8-b369-4e57-b652-eb45256cca36" />
We can also create some alerts if the pipeline fails.

# Serving Layer

The data can be then used to create Dashboards
<img width="2408" height="1490" alt="image" src="https://github.com/user-attachments/assets/68174170-599f-4da7-981e-b95024c311ff" />


# Tools used

(i) Job API: https://api.joinrise.io/api/v1/jobs/
(ii) JSON Storage: Databricks Managed Volumes
(iii) Data Warehousing into fact table and Dimension tables using Spark Declarative Pipeline
(iv) Job scheduler: Databricks job scheduler(Notebook task to fetch data from API) and ETL Pipeline



