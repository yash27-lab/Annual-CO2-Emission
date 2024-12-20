# -*- coding: utf-8 -*-
"""lambda_function

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1A0jb7alKX5MhTVqd28WgwUgO2A4Wx2fv
"""

import boto3
import joblib
import json
import os

# Load the model from S3 bucket
s3 = boto3.client('s3')
BUCKET_NAME = 'co2-model-bucket-final'
MODEL_FILE = 'model.pkl'

# Load the model during Lambda initialization
model = None
def load_model():
    global model
    if model is None:
        with open('/tmp/model.pkl', 'wb') as f:
            s3.download_fileobj(BUCKET_NAME, MODEL_FILE, f)
        model = joblib.load('/tmp/model.pkl')

def lambda_handler(event, context):
    load_model()
    # Parse input from API Gateway
    input_data = json.loads(event['body'])
    features = input_data['features']

    # Make predictions
    prediction = model.predict([features])[0]

    # Return prediction result
    return {
        'statusCode': 200,
        'body': json.dumps({'prediction': prediction})
    }