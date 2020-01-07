import logging
import boto3
import json
from botocore.exceptions import ClientError

bucket_name = 'BUCKET'


def delete_object(bucket_name, object_name):
    """Delete an object from an S3 bucket

    :param bucket_name: string
    :param object_name: string
    :return: True if the referenced object was deleted, otherwise False
    """

    # Delete the object
    s3 = boto3.client('s3')
    try:
        s3.delete_object(Bucket=bucket_name, Key=object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True


def nuke(event, context):
    # get trailing slug
    slug = event['Records'][0]['cf']['request']['uri'].lstrip('/')
    # Don't destroy index
    if slug == 'index.html':
        return

    # Set up logging
    logging.basicConfig(level=logging.DEBUG,
                    format='%(levelname)s: %(asctime)s: %(message)s')

    # Delete the object
    if delete_object(bucket_name, slug):
        logging.info(f'{slug} was deleted from {bucket_name}')
     
    return event['Records'][0]['cf']['response']

if __name__ == '__main__':
    main()
