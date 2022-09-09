import os;
import json;
from http.client import EXPECTATION_FAILED;
from pydoc import cli;
import boto3;



def read_my_credentials(credfile="cred.json"):
    #cf = open(os.getcwd() + '/aws/' + credfile, 'r')
    #using os.getcwd() to get the working directory,this folder path.
    #for security we are saving the sensetive info ,config file under our local and adding /home/.. bath . 
     with open(os.getcwd() + '/boto3/' + credfile, 'r') as cf :
        cred = json.load(cf)
        return cred

cred = read_my_credentials();
   
IAM_client = boto3.client('iam', aws_access_key_id=cred['access-key-id'], 
                                        aws_secret_access_key=cred['secret-access-key'],
                                        region_name=cred['region']);
              

STS_client = boto3.client('sts', aws_access_key_id=cred['access-key-id'], 
                                        aws_secret_access_key=cred['secret-access-key'],
                                        region_name=cred['region']);
   
