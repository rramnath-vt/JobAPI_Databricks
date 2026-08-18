from pyspark import pipelines as dp
from pyspark.sql.functions import col

@dp.table(name="job.target.fact_job",
          table_properties={
        "quality": "gold"
    })
def target_fact_job():
    return(
        spark.readStream.table("silver").select(col("job_id"),col("company_id"),col("job_location_id").alias("location_id"),col("snapshot_date"),col("ingested_datestamp")).distinct()
    )

@dp.materialized_view(name="job.target.usa_job")
def target_usa_job():
    return(
        spark.sql("""
    SELECT DISTINCT
        fact.job_id,                  
        fact.location_id,
        location.location
        from job.target.fact_job fact
        join job.target.dim_location location
        on fact.location_id = location.location_id where lower(location.location) like '%usa' or lower(location.location) like '%united states%' or lower(location.location) like 'usa%'
        """)
        )

@dp.materialized_view(name="job.target.india_job")
def target_india_job():
    return(
        spark.sql("""
    SELECT DISTINCT
        fact.job_id,                  
        fact.location_id,
        location.location
        from job.target.fact_job fact
        join job.target.dim_location location
        on fact.location_id = location.location_id where lower(location.location) like '%india' or lower(location.location) like 'india%'
        """)
        )
