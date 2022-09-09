from appsettings import  IAM_client ;

def client_ProfileData():

    users = IAM_client.list_users();
    print(users);


client_ProfileData();


#
#OUTPUT
#{'UserId': 'AIDAYAEOP4UYASIUU27BX', 'Account': '550054651184', 
# 'Arn': 'arn:aws:iam::550054651184:user/Administrator',
#  'ResponseMetadata': {'RequestId': '56eec070-7a98-4893-9d7d-cde890729061',
#  'HTTPStatusCode': 200, 'HTTPHeaders': 
# {'x-amzn-requestid': '56eec070-7a98-4893-9d7d-cde890729061', 'content-type': 'text/xml', 'content-length': '410',
#  'date': 'Fri, 09 Sep 2022 01:13:45 GMT'}, 'RetryAttempts': 0}}