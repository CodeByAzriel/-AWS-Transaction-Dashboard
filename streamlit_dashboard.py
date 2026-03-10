import streamlit as st
import boto3
import pandas as pd
import io

# AWS S3 config
BUCKET_NAME = "bank-transaction-simulator-ria"
FILE_NAME = "transactions.json"

s3 = boto3.client("s3")

st.title("AWS Transaction Dashboard")

# Load data from S3
@st.cache_data
def load_data():
    obj = s3.get_object(Bucket=BUCKET_NAME, Key=FILE_NAME)
    data = pd.read_json(io.BytesIO(obj['Body'].read()))
    return data

df = load_data()

st.subheader("Transaction Data")
st.dataframe(df)

st.subheader("Summary Stats")
st.write("Total transactions:", len(df))
st.write("Total amount:", df['amount'].sum())
st.write("Transactions by type:")
st.bar_chart(df['type'].value_counts())

st.subheader("Transactions over time")
# Use 'timestamp' instead of 'date'
df['timestamp'] = pd.to_datetime(df['timestamp'])
st.line_chart(df.groupby(df['timestamp'].dt.date)['amount'].sum())