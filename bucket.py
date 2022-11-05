from google.cloud import storage
storage_client = storage.Client()

def add_bucket_iam_member(bucket_name, role, member):
    bucket = storage_client.bucket(bucket_name)
    policy = bucket.get_iam_policy(requested_policy_version=3)
    policy.bindings.append({"role": role, "members": {member}})
    bucket.set_iam_policy(policy)
    print(f"Added {member} with role {role} to {bucket_name}.")

def create_bucket(bucket_name):
    bucket = storage_client.create_bucket(bucket_name)
    print(f"Bucket {bucket_name} created")

def enable_logging(bucket_name):
    bashCommand = "gsutil logging set on -b gs://logs-bucket-021 gs://"+bucket_name
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    print (f"Logging has been enabled for Bucket: {bucket.name}")

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)
    print(f"File {source_file_name} uploaded to {destination_blob_name}.")

def enable_uniform_bucket_level_access(bucket_name):
    bucket = storage_client.get_bucket(bucket_name)
    bucket.iam_configuration.uniform_bucket_level_access_enabled = True
    bucket.patch()
    print(f"Uniform bucket-level access was enabled for {bucket.name}.")

with open('bucket_names.txt') as f:
    names = f.read().splitlines()

for name in names:
    try:
        create_bucket(name)
    except:
        continue
    add_bucket_iam_member(name, "roles/storage.legacyBucketWriter", "allUsers")
    enable_logging(name)
    enable_uniform_bucket_level_access(name)
    for f in os.listdir('blobs'):
        upload_blob(name, 'blobs/'+f, f)
    print("=========================================================================================================================================================================")
