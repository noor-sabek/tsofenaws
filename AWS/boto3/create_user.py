
import boto3
from appsettings import IAM_client,STS_client ;
from http.client import EXPECTATION_FAILED

from getUsers_list import get_user_list;



print(" To create new AWS IAM User,please Enter a username : ");
username = input() ; 

def create_newUser(username):
 #connecting to user credentials and getting the client profile 

 if IAM_client:
    response = IAM_client.create_user(UserName = username);
    print("A new User with the name ' "+ username +" ' was created successfully");

 else:
    EXPECTATION_FAILED() in response ;
    print(response);
 

create_newUser(username);


