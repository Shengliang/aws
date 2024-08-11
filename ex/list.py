import boto3

def list_files(bucket_name, prefix=''):
    """
    List all files in an S3 bucket under a specific prefix.
    """
    s3_client = boto3.client('s3')
    paginator = s3_client.get_paginator('list_objects_v2')
    
    for page in paginator.paginate(Bucket=bucket_name, Prefix=prefix, Delimiter='/'):
        if 'Contents' in page:
            for obj in page['Contents']:
                print(f"{bucket_name}/{obj['Key']}")
        
        # Recursively list objects in subdirectories
        if 'CommonPrefixes' in page:
            for common_prefix in page['CommonPrefixes']:
                list_files(bucket_name, common_prefix['Prefix'])

def main():
    s3 = boto3.resource('s3')
    
    # Print out bucket names
    for bucket in s3.buckets.all():
        print(f"Bucket: {bucket.name}")
        list_files(bucket.name)

if __name__ == "__main__":
    main()

