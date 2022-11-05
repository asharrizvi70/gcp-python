from google.cloud import storage
storage_client = storage.Client()
buckets = storage_client.list_buckets()

def enable_uniform_bucket_level_access(bucket_name):
    bucket = storage_client.get_bucket(bucket_name)

    bucket.iam_configuration.uniform_bucket_level_access_enabled = True
    bucket.patch()

    print(
        f"Uniform bucket-level access was enabled for {bucket.name}."
    )

i=0
for bucket in buckets:
    enable_uniform_bucket_level_access(bucket.name)
    i+=1
print(i)
