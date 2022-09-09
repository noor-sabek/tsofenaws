from http.client import EXPECTATION_FAILED
from appsettings import  IAM_client
from create_user import create_newUser;
import getUsers_list;

print("enter a group name :");
group_name= input(); #"Developers";

print("enter a Policy :");
policy=  input();  #"PowerUserAccess";

print("enter a username :");
user_name= input(); #"developer";
    
ls_Groups = IAM_client.list_groups_for_user(UserName = user_name);
ls_users = getUsers_list.get_user_list;

def create_group_policy(group_name, policy):
    
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

 if (user_name in ls_users & group_name in ls_Groups) :
       response = attach_user_to_group(user_name,group_name);
       print("The groups you have are :    ",ls_Groups['Groups']);
 else:
        if (user_name not in ls_users):
            print("the user is not exist,do you want to create new user? > y/n");
            res = input();

            if(res == "y") : 
                create_newUser(user_name);
                response = attach_user_to_group(user_name,group_name);
                print(AttachUserToGroup);

            else:

                print("please try again later");
                exit();
        else:

                print("the group is not exist,do you want to create new user? > y/n");
                res = input();
 
                if (res == "y") :
                    
                       create_newUser(user_name);
                       response = attach_user_to_group(user_name,group_name);
                       print(AttachUserToGroup);
                else:
                        create_group_policy(response,policy);
                        print("please try again later");
                        exit();



 print(response);


  
    



 AttachpolicyToGroup = IAM_client.attach_group_policy(GroupName=group_name, PolicyArn ='arn:aws:iam::aws:policy/'+ policy);

def attach_user_to_group(user_name, group_name):
    if IAM_client:
        response = IAM_client.add_user_to_group( GroupName=group_name,UserName = user_name);
        print(response)




create_group_policy(group_name, policy);
attach_user_to_group(user_name = user_name, group_name = group_name);

