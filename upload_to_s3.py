import boto3
import os

BUCKET_NAME = "bank-transaction-simulator-ria"  # your S3 bucket
FILE_NAME = os.path.join(os.path.dirname(__file__), "transactions.json")  # always finds the file

s3 = boto3.client("s3")

s3.upload_file(FILE_NAME, BUCKET_NAME, "transactions.json")

print(f"{FILE_NAME} uploaded to S3 bucket {BUCKET_NAME}")