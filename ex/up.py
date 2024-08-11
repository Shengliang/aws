import boto3

# Let's use Amazon S3
s3 = boto3.resource('s3')

# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)


# Upload a new file
with open('list.py', 'rb') as data:
    s3.Bucket('shengliangsong').put_object(Key='code/python/list.py', Body=data)
