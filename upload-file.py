from google.cloud import storage
import os

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    #storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)
    print(f"File {source_file_name} uploaded to {destination_blob_name}.")

storage_client = storage.Client()
buckets = storage_client.list_buckets()
for bucket in buckets:
    for f in os.listdir('blobs'):
        upload_blob(bucket.name, 'blobs/'+f, f)
