import requests
from requests.auth import HTTPDigestAuth
from ipify import get_ip
from pymongo import MongoClient

atlas_group_id = "64d95719ca424a2c6041b5fb"
atlas_api_public_key = "tckzffst"
atlas_api_private_key = "9af5ef90-a76d-4ebb-9d8b-4540e5db6027"
ip = get_ip()

resp = requests.post(
    "https://cloud.mongodb.com/api/atlas/v1.0/groups/{atlas_group_id}/accessList".format(atlas_group_id=atlas_group_id),
    auth=HTTPDigestAuth(atlas_api_public_key, atlas_api_private_key),
    json=[{'ipAddress': ip, 'comment': 'From PythonAnywhere'}]  # the comment is optional
)
if resp.status_code in (200, 201):
    print("MongoDB Atlas accessList request successful", flush=True)
else:
    print(
        "MongoDB Atlas accessList request problem: status code was {status_code}, content was {content}".format(
            status_code=resp.status_code, content=resp.content
        ),
        flush=True
    )


def get_database():

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb+srv://doof_df:Themostevilestever73@doofevilcluster.c60jjqd.mongodb.net/?retryWrites=true&w=majority"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial)
    return client['DoofEvilIncDB']

# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":

    # Get the database
    dbname = get_database()