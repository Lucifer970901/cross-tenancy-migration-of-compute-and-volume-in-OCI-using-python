import oci
import json
import pandas as pd
from pandas import json_normalize
import datetime
import time
import os.path
import concurrent.futures

#provide the configuration details for the old tenancy.
config = oci.config.from_file(file_location="~/.oci/config_sehubjapaciaasset01")
par_url_lst =[]

object_storage_client = oci.object_storage.ObjectStorageClient(config)
get_namespace_response = object_storage_client.get_namespace(compartment_id=config["compartment_id"])
bucket_name="image_backup"

def bucket_exists(bucket_name):
    try:
        object_storage_client.get_bucket(namespace_name=get_namespace_response.data, bucket_name=bucket_name)
        return True
    except oci.exceptions.ServiceError as e:
        if e.status == 404:
            return False  # Bucket does not exist
        else:
            raise e  # Other error​

if bucket_exists(bucket_name):
    #list objects
    list_objects_response = object_storage_client.list_objects(
    namespace_name=get_namespace_response.data,
    bucket_name="image_backup")
    for objects in list_objects_response.data.objects:
        create_preauthenticated_request_response = object_storage_client.create_preauthenticated_request(
        namespace_name=get_namespace_response.data,
        bucket_name=bucket_name,
        create_preauthenticated_request_details=oci.object_storage.models.CreatePreauthenticatedRequestDetails(
        name="PAR_" + objects.name,
        access_type="ObjectRead",
        time_expires=(datetime.datetime.now() + datetime.timedelta(hours=72)),
        object_name=objects.name))
        par_url_lst.append([create_preauthenticated_request_response.data.full_path, create_preauthenticated_request_response.data.name])

print(par_url_lst)

df = pd.DataFrame(par_url_lst, columns=["custom_image_URL", "custom_image_name"])
df = df.dropna()
df.to_csv("custom_image_PAR_details.csv")
print(df)
