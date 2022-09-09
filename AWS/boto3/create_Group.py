from email import policy
from http.client import EXPECTATION_FAILED
from appsettings import  IAM_client
import os;
from create_user import create_newUser;
import getUsers_list


global ls_Groups;
global userName;
ls_users = getUsers_list.get_user_list;


def create_group(group_name):
    
 if IAM_client:
        groups = IAM_client.list_groups();
        while group_name in groups:
            print(f"The group: {group_name} is already exists, please try again");
            print(" !! TRY AGAIN !! please enter another Group name:") 
            group_name = input();

        print("The new group is : ",group_name);   
        response = IAM_client.create_group(GroupName = group_name);
        print(response);

 else:
        EXPECTATION_FAILED() in response ;
        print(response);




def AttachUserToGroup(user_name,group_name):
 ls_Groups = IAM_client.list_groups_for_user(UserName = userName);
 
 if (user_name in ls_users & group_name in ls_Groups) :
       response = IAM_client.add_user_to_group( GroupName = group_name,UserName = user_name);
       print("The groups you have are :    ",ls_Groups['Groups']);
 else:
        if (user_name not in ls_users):
            print("the user is not exist,do you want to create new user? > y/n");
            res = input();

            if(res == "y") : 
                create_newUser(user_name);
                response = IAM_client.add_user_to_group( GroupName=group_name,UserName = user_name);
                AttachpolicyToGroup = IAM_client.attach_group_policy(GroupName=group_name, PolicyArn ='arn:aws:iam::aws:policy/'+ policy['Statement'][0]['Sid ']);

                print("your data is : ",AttachUserToGroup,response);

            else:

                print("please try again later");
                exit();
        else:

                print("the group is not exist,do you want to create new user? > y/n");
                res = input();
 
                if (res == "y") :
                    
                       newuser = create_newUser(user_name);
                       response = IAM_client.add_user_to_group( GroupName=group_name,UserName = user_name);
                       print(AttachUserToGroup);
                else:
                        print("please try again later");
                        exit();



 print(response);






create_group();
AttachUserToGroup();

