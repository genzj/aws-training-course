import boto3
import os
import sys
import base64
import uuid
import logging

L = logging.getLogger(__name__)
L.setLevel(logging.DEBUG)

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    L.info('event %s', event)
    L.info('context %s', context)
    bucket = 'zj001-photo-resized'
    key = event['imageKey']
    download_path = '/tmp/{}{}'.format(uuid.uuid4(), key)
    L.info('ready to download %s/%s to %s', bucket, key, download_path)
    s3_client.download_file(bucket, key, download_path)
    with open(download_path, 'rb') as photo:
        return base64.b64encode(photo.read()).decode('ascii')

