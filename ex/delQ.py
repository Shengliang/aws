import boto3

# Create SQS client
sqs = boto3.client('sqs')

# Delete SQS queue
# sqs.delete_queue(QueueUrl='SQS_QUEUE_URL')
sqs.delete_queue(QueueUrl='SQS_QUEUE_NAME')
