# flight-price-MLproject #



pip install -r requirements.txt ---

-e .  --- installs project Store_sales

mailid = pbannuru@gmail.com

herokukey = f2ccae77-156e-4e59-be69-59531739708c

app name = flight-fare-ml




Software and account Requirement.
Github Account
Heroku Account
VS Code IDE
GIT cli
GIT Documentation
Creating conda environment

conda create -p venv python==3.7 -y
conda activate venv/
OR

conda activate venv
pip install -r requirements.txt
To Add files to git

git add .
OR

git add <file_name>
Note: To ignore file or folder from git we can write name of file/folder in .gitignore file

To check the git status

git status
To check all version maintained by git

git log
To create version/commit all changes by git

git commit -m "message"
To send version/changes to github

git push origin main
To check remote url

git remote -v
To setup CI/CD pipeline in heroku we need 3 information

HEROKU_EMAIL = pbannuru@gmail.com
HEROKU_API_KEY = <>
HEROKU_APP_NAME = ml-regression-app
BUILD DOCKER IMAGE

docker build -t <image_name>:<tagname> .  ===   docker build -t store_sales:project . 
Note: Image name for docker must be lowercase

To list docker image
"""
docker images

"""
Run docker image

docker run -p 5000:5000 -e PORT=5000 3cc46b1667f9
To check running container in docker

docker ps
Tos stop docker conatiner

docker stop <container_id>
python setup.py install
Install ipykernel

pip install ipykernel

create folder .github and another folder = workflows -- create main.yaml file




Data Drift: When your datset stats gets change we call it as data drift

Write a function to get training file path from artifact dir
