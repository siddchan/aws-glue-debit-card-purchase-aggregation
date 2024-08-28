import boto3

s3 = boto3.client("s3")
bucket_name = "aws-glue-debit-card-purchase-aggregation"


def upload_to_s3(filename, date_str):
    """Uploads a CSV file to S3 with Hive-style partitioning"""
    file_path = f"raw_data/date={date_str}/{filename}"  # Hive-style partitioning
    s3.upload_file(f'/tmp/{filename}', bucket_name, file_path)
    print(f"File uploaded to S3 Bucket {bucket_name}/{file_path}")
    return