from pyspark import pipelines as dp
from pyspark.sql.functions import *

@dp.table(name="job_dim_source")
def job_dim_source():
    return (
        dp.read_stream("silver")
        .select(
            col("job_id"),
            col("job_type").alias("type"),
            col("job_title").alias("title"),
            col("job_slug").alias("slug"),
            col("job_url").alias("url"),
            col("createdAt").cast("timestamp").alias("createdAt"),
            col("updatedAt").cast("timestamp").alias("updatedAt")
        )
    )

dp.create_streaming_table(
    "job.target.dim_job",
    table_properties={
        "quality": "gold"
    }
)

dp.create_auto_cdc_flow(
    target="job.target.dim_job",
    source="job_dim_source",
    keys=["job_id"],
    sequence_by=col("updatedAt"),
    stored_as_scd_type=2
)

@dp.table(name="job.target.dim_badge",
    table_properties={
        "quality": "gold"
    })
def dimbadge():
    return (
        dp.read_stream("silver")
        .select("job_id",explode("owner_badges").alias("badges")).distinct())

@dp.table(name="job.target.dim_benefits",
    table_properties={
        "quality": "gold"
    })
def dimbenefits():
    return (
        dp.read_stream("silver")
        .select("job_id",explode("owner_benefits").alias("benefits")).distinct())

@dp.table(name="job.target.dim_company",table_properties={
        "quality": "gold"
    })
def dim_company():
    return (
        dp.read_stream("silver").select(col("company_id"),col("company_name").alias("name"),col("company_location").alias("location"),col("company_role").alias("role"),col("company_photo").alias("photo")).distinct()
        )

@dp.table(name="job.target.dim_location",table_properties={
        "quality": "gold"
    })
def dim_location():
    return (
        dp.read_stream("silver").select(col("job_location_id").alias("location_id"),col("job_location").alias("location"),col("latitude"),col("longitude")).distinct()
        )