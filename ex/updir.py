import os
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

def upload_python_files_to_s3(directory, bucket_name, s3_path):
    # Initialize the S3 resource
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)

    try:
        # Iterate through all files in the directory
        for root, dirs, files in os.walk(directory):
            for file_name in files:
                if file_name.endswith('.py') or  file_name.endswith('.sh'):
                    # Full path to the file
                    full_file_path = os.path.join(root, file_name)
                    
                    # S3 key path (relative to the root of the directory)
                    relative_path = os.path.relpath(full_file_path, directory)
                    s3_key = f"{s3_path}/{relative_path.replace(os.sep, '/')}"
                    
                    # Upload the file
                    with open(full_file_path, 'rb') as data:
                        bucket.put_object(Key=s3_key, Body=data)
                    
                    print(f"File '{full_file_path}' successfully uploaded to '{s3_key}'.")

    except FileNotFoundError:
        print(f"The directory '{directory}' was not found.")
    except NoCredentialsError:
        print("AWS credentials not available.")
    except PartialCredentialsError:
        print("Incomplete AWS credentials provided.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
directory = "."  # Replace with your directory path
bucket_name = "shengliangsong"         # Replace with your S3 bucket name
s3_path = "code/python"

upload_python_files_to_s3(directory, bucket_name, s3_path)

