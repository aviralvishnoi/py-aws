"""s3_parser
Usage:
  python s3_parser.py <bucket_name>
"""
import sys
import boto3


def get_s3_file_location(bucket_name):
    """
    Lists all the keys available in s3 bucket
    :param bucket_name (str): s3 bucket for which you want to list the keys
    :return: all_keys (list): list of all the keys available in s3 bucket
    """
    client = boto3.client('s3')
    response = client.list_objects(
        Bucket=bucket_name
    )
    all_keys = []
    contents = response.get('Contents', None)
    if contents:
        for item in contents:
            key = contents.get('Key', None)
            if key:
                all_keys.append(key)
    else:
        print('Nothing returned while list objects in s3 bucket')
    return all_keys


if __name__ == '__main__':
    bucket_name = sys.argv[1]
    print(bucket_name)
    if bucket_name:
        get_s3_file_location(bucket_name)
    else:
        print('Pass the bucket name properly')