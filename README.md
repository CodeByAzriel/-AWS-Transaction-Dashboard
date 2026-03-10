# -AWS-Transaction-Dashboard
A Python-based project that simulates bank transactions, uploads them to an AWS S3 bucket, and visualizes them in a Streamlit dashboard.
<img width="1588" height="871" alt="image" src="https://github.com/user-attachments/assets/0fb62353-eb6c-4c62-b9cd-a868d8965606" />

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup & Installation](#setup--installation)
- [Usage](#usage)
- [Folder Structure](#folder-structure)
- [Contributing](#contributing)
- [License](#license)

---

## Overview
This project is designed to simulate banking transactions and provide a visual representation of transaction data. The workflow is as follows:

1. Simulate transaction data with Python.
2. Upload transactions to an AWS S3 bucket.
3. Display data and charts using a Streamlit dashboard.

This project is ideal for learning about **Python automation**, **AWS S3 integration**, and **data visualization**.

---

## Features
- Generate simulated transaction data (`transactions.json`).
- Upload data to AWS S3.
- Visualize transactions with interactive charts using Streamlit.
- Modular Python scripts for easy extension.

---

## Technologies Used
- Python 3.10
- Boto3 (AWS SDK for Python)
- Streamlit
- AWS S3
- JSON for data storage
- Git & GitHub

---

## Setup & Installation

1. **Clone the repository**  
```bash
git clone <your-repo-url>
cd aws-transaction-dashboard
Technologies Used

Python 3.10

Boto3 (AWS SDK for Python)

Streamlit

AWS S3

JSON for data storage

Git & GitHub

Setup & Installation

Clone the repository

git clone <repo-url>
cd aws-transaction-dashboard

Create a virtual environment (optional but recommended)

python -m venv venv
# Activate the environment
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

Install dependencies

pip install -r requirements.txt

Configure AWS CLI

aws configure
Enter your AWS Access Key ID, Secret Access Key, default region (e.g., eu-north-1), and output format (json). Make sure the S3 bucket exists.

Usage

Simulate Transactions

python simulate_transactions.py

Generates transactions.json in the transaction_simulator folder.

Upload Transactions to S3

python upload_to_s3.py

Uploads transactions.json to the specified AWS S3 bucket.

Run Streamlit Dashboard

streamlit run dashboard.py

Open the URL in the terminal to view interactive charts.

Folder Structure
aws-transaction-dashboard/
│
├── transaction_simulator/
│   ├── simulate_transactions.py    # Generates transaction data
│   ├── transactions.json           # Generated JSON data
│   └── upload_to_s3.py             # Uploads JSON to AWS S3
│
├── dashboard/
│   └── dashboard.py                # Streamlit dashboard
│
├── requirements.txt                # Python dependencies
└── README.md                       # Project documentation
Contributing

Fork the repository.

Create a branch:

git checkout -b feature/YourFeature

Make changes and commit:

git commit -m "Add feature"

Push to branch:

git push origin feature/YourFeature

Open a Pull Request.
