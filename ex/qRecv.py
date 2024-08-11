
import boto3
import argparse

def receive_messages_from_sqs(queue_url, number_of_messages):
    # Create SQS client
    sqs = boto3.client('sqs')

    try:
        # Receive messages from SQS queue
        response = sqs.receive_message(
            QueueUrl=queue_url,
            AttributeNames=['SentTimestamp'],
            MaxNumberOfMessages=number_of_messages,
            MessageAttributeNames=['All'],
            VisibilityTimeout=0,
            WaitTimeSeconds=0
        )

        # Check if any messages were received
        if 'Messages' not in response:
            print('No messages received.')
            return

        # Process each message
        for message in response['Messages']:
            receipt_handle = message['ReceiptHandle']
            
            # Print received message
            print('Received message: %s' % message)
            
            # Delete received message from queue
            sqs.delete_message(
                QueueUrl=queue_url,
                ReceiptHandle=receipt_handle
            )
            print('Deleted message with ReceiptHandle: %s' % receipt_handle)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Receive and delete messages from an SQS queue.")
    parser.add_argument('-q', '--queue_url', required=True, help="SQS queue URL.")
    parser.add_argument('-n', '--number_of_messages', type=int, default=1, help="Number of messages to receive.")
    args = parser.parse_args()

    # Call the function with provided arguments
    receive_messages_from_sqs(args.queue_url, args.number_of_messages)

