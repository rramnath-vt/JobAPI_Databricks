from pyspark import pipelines as dp
from pyspark.sql.functions import *

@dp.table(name="bronze")
def my_table():
    df = spark.readStream.format("cloudFiles") \
        .option("cloudFiles.format", "json") \
        .option("cloudFiles.inferColumnTypes", "true") \
        .option("cloudFiles.schemaEvolutionMode", "addNewColumns") \
        .load("/Volumes/job/source/job_volume/job_api_scrapper/")
    jobs_df = df.select(explode(col("result.jobs")).alias("jobs"))
    jobs_flat_df = jobs_df.select("jobs.*").withColumn("ingested_datestamp", current_timestamp()).withColumn("snapshot_date", col("ingested_datestamp").cast("date"))
    return jobs_flat_df

@dp.table(name="silver")
def my_table():
    df = spark.readStream.table("bronze")
    df_enriched_silver = df.select(
    col("_id").alias("job_id"),
    col("map.locationName").alias("job_location"),
    col("map.lat").alias("latitude"),
    col("map.lng").alias("longitude"),
    col("title").alias("job_title"),
    col("slug").alias("job_slug"),
    col("url").alias("job_url"),
    col("owner._id").alias("company_id"),
    col("owner.companyName").alias("company_name"),
    col("owner.location").alias("company_location"),
    col("owner.role").alias("company_role"),
    col("type").alias("job_type"),
    col("owner.photo").alias("company_photo"),
    col("updatedAt"),
    col("createdAt"),
    col("owner.benefits.benefits").alias("owner_benefits"),
    col("owner.badges").alias("owner_badges"),
    col("ingested_datestamp"),
    col("snapshot_date")
).withColumn("owner_benefits", when(size(col("owner_benefits")) > 0, col("owner_benefits")).otherwise(None)).withColumn("owner_badges", when(size(col("owner_badges")) > 0, col("owner_badges")).otherwise(None)).withColumn("job_location_id",
    sha2(coalesce(concat_ws("_", col("latitude").cast("string"), col("longitude").cast("string")), lit("unknown")), 256))
    return df_enriched_silver
    