import boto3;
import appsettings
from appsettings import IAM_client;


def get_user_list():
    users = IAM_client.list_users();
    print(users);
    return users;


get_user_list();