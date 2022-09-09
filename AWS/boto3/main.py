from http.client import EXPECTATION_FAILED
from appsettings import  IAM_client
import os;
from create_user import create_newUser;
import getUsers_list
from ..security.get_policyFile import Get_policyFile;
from create_Group import create_group, AttachUserToGroup


print("enter a group name :");
group_name= input(); #"Developers";

print(" the Policy :" );
policy = Get_policyFile();

print("enter a username :");
user_name= input(); #"developer";
    


create_group(group_name, policy,user_name);
    
AttachUserToGroup(user_name,group_name);

create_newUser();


