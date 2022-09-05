import boto3
import json


def demo_boto3():
    creds = json.load(open('/home/osboxes/Documents/cred.json', 'r'))
    client = boto3.client('iam', aws_access_key_id=creds['access-key-id'],
                                  aws_secret_access_key=creds['secret-access-key'],
                                  region_name=creds['region'])
    users = client.list_users()
    print(users)

demo_boto3()
