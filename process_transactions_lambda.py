import json
import boto3
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Transactions')  # Make sure table exists

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    response = s3.get_object(Bucket=bucket, Key=key)
    transactions = json.loads(response['Body'].read())
    
    for txn in transactions:
        if txn['amount'] > 1500:
            print(f"ALERT: Large transaction detected: {txn}")
            
        table.put_item(
            Item={
                'transaction_id': str(txn['transaction_id']),
                'account_id': str(txn['account_id']),
                'transaction_type': txn['transaction_type'],
                'amount': Decimal(str(txn['amount'])),
                'timestamp': txn['timestamp']
            }
        )
        
    return {
        'statusCode': 200,
        'body': json.dumps('Transactions processed successfully')
    }