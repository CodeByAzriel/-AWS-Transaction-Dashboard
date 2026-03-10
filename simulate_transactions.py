import boto3

BUCKET_NAME = "bank-transaction-simulator-ria-001"  # Your S3 bucket name
FILE_NAME = "transactions.json"

s3 = boto3.client("s3")

s3.upload_file(FILE_NAME, BUCKET_NAME, FILE_NAME)

print(f"{FILE_NAME} uploaded to S3 bucket {BUCKET_NAME}")