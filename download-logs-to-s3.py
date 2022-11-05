from google.cloud import storage
import os, subprocess, datetime, boto3

client = boto3.client("s3")
x=datetime.datetime.utcnow()
storage_client = storage.Client()
buckets = storage_client.list_buckets()

for bucket in buckets:
    if bucket.name == 'logs-bucket-021':
        continue
    try:
        file_name = bucket.name+"_usage_"+x.strftime("%Y_%m_%d_%H*")
        bashCommand = "gcloud storage cp gs://logs-bucket-021/"+file_name+" /home/ubuntu/Downloaded_blobs/"
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        client.upload_file('/home/ubuntu/Downloaded_blobs/'+file_name,'',bucket.name+x.strftime("-%d-%m-%Y-[%H:00]"))
    except:
        continue
for i in os.listdir('/home/ubuntu/Downloaded_blobs/'):
    try:
        os.remove('/home/ubuntu/Downloaded_blobs/'+i)
    except:
        continue
