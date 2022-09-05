import os
from urllib import response
import boto3
import json


def read_my_credentials(credfile="cred.json"):
    #cf = open(os.getcwd() + '/aws/' + credfile, 'r')
    #using os.getcwd() to get the working directory,this folder path.
    #for security we are saving the sensetive info ,config file under our local and adding /home/.. bath . 
    cf = open('/home/osboxes/Documents/cred.json', 'r')
    creds = json.load(cf)
    return creds


def Add_myUser():

 creds = read_my_credentials();
 client = boto3.client('iam', aws_access_key_id=creds['access-key-id'],
                                  aws_secret_access_key=creds['secret-access-key'],
                                  region_name=creds['region'])


 response = client.create_user(UserName='aml');
print(response.__name__);


Add_myUser()
