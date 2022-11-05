from google.cloud import storage
import subprocess, datetime
x=datetime.datetime.utcnow()
storage_client = storage.Client()
buckets = storage_client.list_buckets()
log_bucket = storage_client.bucket('logs-bucket-021')
for bucket in buckets:
    if bucket.name == 'logs-bucket-021':
        continue
    file_name = bucket.name+"_usage_"+x.strftime("%Y_%m_%d_%H*")
    try:
    	blob = bucket.blob(file_name)
    	blob.download_to_filename('Downloaded_blobs/'+file_name)    
    except:
        continue
