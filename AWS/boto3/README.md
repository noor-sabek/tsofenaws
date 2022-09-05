# boto3

The famous aws python sdk library.

## Documentation

- Go to the [latest docs](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html).
- Go to [the pip installation page](https://pypi.org/project/boto3/).

##  Installaion

- Create a new virtual environment:  
(to be compatible with this git repository, use **venv** as a name)  
**python3 -m venv \<virtual env name\>**
- Activate the virtual environment:  
**source \<virtual env name\>/bin/activate**
- Install:  
**pip install boto3**

## Creating a json credentials file

- Use **cred.json** to be compatible with this repository
- You can create this file by simply running:  
**aws sts get-caller-identity** and embedding the output into the file.

