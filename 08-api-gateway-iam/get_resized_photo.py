import base64
import logging
import uuid

import boto3

L = logging.getLogger(__name__)
L.setLevel(logging.DEBUG)

s3_client = boto3.client('s3')


def lambda_handler(event, context):
    L.info('event %s', event)
    L.info('context %s', vars(context))
    bucket = 'zj001-image-resized'
    key = event['requestContext']['identity']['userArn'].split('/')[-1] \
        + '/' \
        + event['queryStringParameters']['filename']
    download_path = '/tmp/{}{}'.format(uuid.uuid4(), key.replace('/', '---'))
    L.info('ready to download %s/%s to %s', bucket, key, download_path)
    s3_client.download_file(bucket, key, download_path)
    with open(download_path, 'rb') as photo:
        return {
            "statusCode": 200,            # a valid HTTP status code
            "headers": {
                "Content-Type": "image/jpeg"  # any API-specific custom header
            },
            # a JSON string / base64 encoded string.
            "body": base64.b64encode(photo.read()).decode('ascii'),
            "isBase64Encoded":  True  # for binary support
        }
