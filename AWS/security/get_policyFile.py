import os;
import json;
from boto3 import IAM_client ;

def Get_policyFile(policy_name = 'policy.json'):

    try:
                with open(os.getcwd() +policy_name+ 'r') as f:

                    policy = json.load(f);
                    policy = json.dumps(policy);
                    print("policy was created");

                    return IAM_client.create_policy(
                        PolicyName=policy_name, PolicyDocument=policy);

    except FileNotFoundError as e:
                print(f"file not found: {e}")
                return;  


Get_policyFile();