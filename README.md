AWS-Transaction-Dashboard

A Python-based project that simulates bank transactions, uploads them to an AWS S3 bucket, and visualizes them in a Streamlit dashboard.

<img width="1588" height="871" alt="image" src="https://github.com/user-attachments/assets/0fb62353-eb6c-4c62-b9cd-a868d8965606" />
Table of Contents

Overview

Features

Technologies Used

Setup & Installation

Usage

Folder Structure

Contributing

License

Overview

This project simulates banking transactions and provides a visual representation of transaction data. The workflow is:

Simulate transaction data with Python.

Upload transactions to an AWS S3 bucket.

Display data and charts using a Streamlit dashboard.

It’s perfect for learning Python automation, AWS S3 integration, and data visualization.

Features

Generate simulated transaction data (transactions.json).

Upload data to AWS S3.

Visualize transactions with interactive charts using Streamlit.

Modular Python scripts for easy extension.

Technologies Used

Python 3.10

Boto3 (AWS SDK for Python)

Streamlit

AWS S3

JSON for data storage

Git & GitHub

Setup & Installation

Clone the repository

git clone <your-repo-url>
cd aws-transaction-dashboard

Create a virtual environment (optional but recommended)

python -m venv venv
# Activate environment
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

python transaction_simulator/simulate_transactions.py

Generates transactions.json in the transaction_simulator folder.

Upload Transactions to S3

python transaction_simulator/upload_to_s3.py

Uploads transactions.json to the specified AWS S3 bucket.

Run Streamlit Dashboard

streamlit run dashboard/dashboard.py

Open the URL shown in the terminal to view interactive charts.

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

License

This project is licensed under the MIT License. See LICENSE
 for details.
