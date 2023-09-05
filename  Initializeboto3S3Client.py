from flask import Flask
app = Flask(__name__)
import boto3

app = Flask(__name__)

# Initialize a boto3 S3 client
s3 = boto3.client('s3', region_name='eu-north-1')

# Define your routes and functions here
