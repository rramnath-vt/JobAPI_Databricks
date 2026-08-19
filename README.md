# JobAPI_Databricks

This is an end-to-end data engineering project that was developed using Databricks. The objective of this project is to fetch job posting details from a job api like joinrise and gather valuable insights of the job listings to analyze job trends

# Sample Architecture

<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/0c3960aa-4361-495e-91c4-e750cff15917" />

# Data Warehouse Design

<img width="1516" height="1128" alt="image" src="https://github.com/user-attachments/assets/9f105df5-779e-45f7-b141-b6af09475c01" />
Design Principle: Created job dimension using Slowly Changing Dimension 2 sequenced by updatedAt date column that captures any changes to the job title, job role etc.


# Data Lineage

<img width="1776" height="1072" alt="image" src="https://github.com/user-attachments/assets/1498d5b5-b013-4741-92c2-eb510ad3698e" />

# Job Scheduler

<img width="1416" height="574" alt="image" src="https://github.com/user-attachments/assets/87678fe8-b369-4e57-b652-eb45256cca36" />
The job is scheduled to run at 17:00 Central Time everyday to gather the job details of the entire day. Dashboard will be refreshed after successful refresh of the tables.

# Serving Layer

The data can be then used to create Dashboards
<img width="2408" height="1490" alt="image" src="https://github.com/user-attachments/assets/68174170-599f-4da7-981e-b95024c311ff" />

# AI Integration

<img width="1666" height="1320" alt="image" src="https://github.com/user-attachments/assets/629abc5a-e278-4fe2-9141-b28d4ca0ce8f" />
Created an AI agent using LangChain to analyze the Databricks table and generate results using natural language. Model used - Gemini 3.5 Flash


# Tools used

(i) Job API: https://api.joinrise.io/api/v1/jobs/
(ii) JSON Storage: Databricks Managed Volumes
(iii) Data Warehousing into fact table and Dimension tables using Spark Declarative Pipeline
(iv) Job scheduler: Databricks job scheduler(Notebook task to fetch data from API) and ETL Pipeline



