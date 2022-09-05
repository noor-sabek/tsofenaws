
from urllib import response
import os
import boto3
import json



def read_my_credentials(credfile="cred.json"):
    cf = open('/home/osboxes/Documents/' + credfile, 'r')
    creds = json.load(cf)
    return creds

    
creds = read_my_credentials();

def demo_boto3():
    client = boto3.client('sts', aws_access_key_id=creds['access-key-id'],
                                      aws_secret_access_key=creds['secret-access-key'],
                                      region_name=creds['region']);

    user=(client.get_caller_identity());
    print(user);



def get_user_list():
    client = boto3.client('sts', aws_access_key_id=creds['access-key-id'],
                                      aws_secret_access_key=creds['secret-access-key'],
                                      region_name=creds['region']);
    users = client.list_users()
    print(users)


demo_boto3()
get_user_list()